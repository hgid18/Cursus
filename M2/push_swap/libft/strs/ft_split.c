/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 16:28:10 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/12/11 15:34:59 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	ft_initiate_vars(size_t *i, int *j, int *start)
{
	*i = 0;
	*j = 0;
	*start = -1;
}

static void	*free_all(char **strs, int count)
{
	int	i;

	i = 0;
	while (i < count)
	{
		free(strs[i]);
		i++;
	}
	free(strs);
	return (NULL);
}

static int	count_words(const char *str, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*str)
	{
		if (*str != c && in_word == 0)
		{
			in_word = 1;
			count++;
		}
		else if (*str == c)
			in_word = 0;
		str++;
	}
	return (count);
}

char	**ft_split(const char *s, char c)
{
	char	**res;
	size_t	i;
	int		j;
	int		start;

	ft_initiate_vars(&i, &j, &start);
	res = ft_calloc((count_words(s, c) + 1), sizeof(char *));
	if (!res)
		return (NULL);
	while (i <= ft_strlen(s))
	{
		if (s[i] != c && start < 0)
			start = i;
		else if ((s[i] == c || i == ft_strlen(s)) && start >= 0)
		{
			res[j] = ft_substr(s, start, i - start);
			if (!(res[j]))
				return (free_all(res, j));
			start = -1;
			j++;
		}
		i++;
	}
	return (res);
}

/*#include <stdio.h>
int main(void)
{
	char **result;
	char *str = "Howling outside your door";
	char sep = ' ';
	int i = 0;

	result = ft_split(str, sep);
	if (!result)
	{
		printf("Error: ft_split devolvió NULL\n");
		return 1;
	}

	printf("Probando ft_split con la cadena: 
	\"%s\" y separador '%c'\n\n", str, sep);
	
	while (result[i])
	{
		printf("Palabra %d: %s\n", i, result[i]);
		free(result[i]);
		i++;
	}
	free(result);
	
	return 0;
}
*/