/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:18:47 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 16:23:33 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*calloc(size_t nmemb, size_t size)
{
	char	*str;
	int		i;

	i = 0;
	str = malloc(nmemb * size);
	if (!str)
	{
		free(str);
		return (NULL);
	}
	ft_bzero(str, nmemb * size);
	return (str);
}
