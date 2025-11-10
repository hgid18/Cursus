/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:02:42 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 16:08:24 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	ldest;
	size_t	lsrc;
	size_t	tlen;

	ldest = ft_strlen(dst);
	lsrc = ft_strlen(src);
	tlen = 0;
	i = 0;
	if (ldest < size)
		tlen = ldest + lsrc;
	else
		tlen = lsrc + size;
	while (src[i] && (ldest + 1) < size)
	{
		dst[ldest] = src[i];
		i++;
		ldest++;
	}
	dst[ldest] = '\0';
	return (tlen);
}
