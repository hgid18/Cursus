/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:45:31 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 18:46:22 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t		i;
	char		*sd;
	const char	*sc;

	sd = (char *)dest;
	sc = (const char *)src;
	if (dest < src)
	{
		i = n + 1;
		while (--i > 0)
			sd[i] = sc[i];
	}
	else
	{
		i = -1;
		while (++i < n)
			sd[i] = sc[i];
	}
	return (sd);
}
