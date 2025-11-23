/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:45:31 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/14 18:14:36 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t	i;
	char	*sd;
	char	*sc;

	i = -1;
	if (!dest && !src)
		return (NULL);
	sd = (char *)dest;
	sc = (char *)src;
	if (sd > sc)
		while (n--)
			sd[n] = sc[n];
	else
		while (++i < n)
			sd[i] = sc[i];
	return (dest);
}
