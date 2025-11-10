/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:03:30 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 16:18:16 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	while (big[i] && i < len)
	{
		j = 0;
		if (big[i + j] == little[j])
		{
			if (!little[j])
				return ((unsigned char *)big + i);
			j++;
		}
		i++;
	}
	return (NULL);
}
