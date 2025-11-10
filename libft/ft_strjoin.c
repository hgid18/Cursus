/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 18:18:58 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 18:49:43 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	tlen;
	size_t	i;
	size_t	j;
	char	*str;

	i = 0;
	j = 0;
	tlen = ft_strlen(s1) + ft_strlen(s2);
	str = malloc(tlen * sizeof(char));
	while (str[i] && i < ft_strlen(s1))
	{
		str[i] = s1[i];
		i++;
	}
	while (str[i + j] && i + j < tlen)
	{
		str[i + j] = s2[j];
		j++;
	}
	return (str);
}
