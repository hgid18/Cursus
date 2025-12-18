/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/20 13:06:48 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/12/02 13:33:10 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_parse_line(char *aux)
{
	int		i;
	char	*line;
	int		j;

	if (!aux || aux[0] == '\0')
		return (NULL);
	i = 0;
	while (aux[i] && aux[i] != '\n')
		i++;
	line = malloc((i + 2) * sizeof(char));
	if (!line)
		return (NULL);
	j = 0;
	while (aux[j] && aux[j] != '\n')
	{
		line[j] = aux[j];
		j++;
	}
	if (aux[j] == '\n')
		line[j++] = '\n';
	line[j] = '\0';
	return (line);
}

char	*ft_update(char *line)
{
	int		i;
	int		j;
	char	*new_line;
	size_t	remaining_len;

	if (!line)
		return (NULL);
	i = 0;
	while (line[i] && line[i] != '\n')
		i++;
	if (!line[i])
		return (free(line), NULL);
	remaining_len = ft_strlen(line + i + 1);
	new_line = malloc(remaining_len + 1);
	if (!new_line)
		return (free(line), NULL);
	if (line[i] == '\n')
		i++;
	j = 0;
	while (line[i])
		new_line[j++] = line[i++];
	new_line[j] = '\0';
	free(line);
	return (new_line);
}

static char	*ft_read(int fd, char *aux)
{
	char	*buff;
	int		r;

	if (fd < 0)
		return (NULL);
	buff = malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buff)
		return (free(aux), NULL);
	r = 1;
	while (!ft_strchr(aux, '\n') && r > 0)
	{
		r = read(fd, buff, BUFFER_SIZE);
		if (r < 0)
			return (free(aux), free(buff), NULL);
		buff[r] = '\0';
		aux = ft_strjoin(aux, buff);
		if (!aux)
			return (free(buff), NULL);
	}
	return (free(buff), aux);
}

char	*get_next_line(int fd)
{
	static char	*buff;
	char		*aux;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (free(buff), NULL);
	if (!buff)
	{
		buff = malloc(1);
		if (!buff)
			return (NULL);
		buff[0] = '\0';
	}
	buff = ft_read(fd, buff);
	if (!buff)
		return (free(buff), NULL);
	aux = ft_parse_line(buff);
	if (!aux)
	{
		free(buff);
		buff = NULL;
		return (NULL);
	}
	buff = ft_update(buff);
	return (aux);
}
