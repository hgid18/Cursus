/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/20 13:06:48 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/23 11:45:15 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_parse_line(char *aux)
{
	int		i;
	char	*line;
	int		j;

	i = 0;
	j = 0;
	if (!aux || aux[0] == '\0')
		return (NULL);
	while (aux[i] && aux[i] != '\n')
		i++;
	line = malloc((i + 1) * sizeof(char));
	if (!line)
		return (NULL);
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

	i = 0;
	j = 0;
	if (!line)
		return (NULL);
	while (line[i] && line[i] != '\n')
		i++;
	if (!line[i])
	{
		free(line);
		return (NULL);
	}
	new_line = malloc(((ft_strlen(line) - i) + 1) * sizeof(char));
	if (!new_line)
		return (NULL);
	if (line[i] == '\n')
		i++;
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

	buff = malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buff)
		return (NULL);
	r = 1;
	while (!ft_strchr(aux, '\n') && r > 0)
	{
		r = read(fd, buff, BUFFER_SIZE);
		if (r < 0)
		{
			free(buff);
			return (NULL);
		}
		buff[r] = '\0';
		aux = ft_strjoin(aux, buff);
		if (!aux)
			return (NULL);
	}
	free(buff);
	return (aux);
}

char	*get_next_line(int fd)
{
	static char	*buff;
	char		*aux;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (!buff)
	{
		buff = malloc(sizeof(char));
		if (!buff)
			return (NULL);
		buff[0] = '\0';
	}
	buff = ft_read(fd, buff);
	if (!buff)
		return (NULL);
	aux = ft_parse_line(buff);
	buff = ft_update(buff);
	return (aux);
}

/*int	main(int argc, char **argv)
{
	int		fd;
	char	*line;
	
	(void)argc;
	fd = open(argv[1], O_RDONLY);
	if (fd < 0)
		return (0);
	while ((line = get_next_line(fd)) != NULL)
	{
		printf("%s", line);
		free(line);
	}
	close(fd);
}*/