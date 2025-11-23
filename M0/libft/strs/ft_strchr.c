/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:18:32 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/14 18:48:54 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(char *str, int c)
{
	int	i;

	i = -1;
	while (str[++i])
	{
		if (str[i] == (char)c)
			return ((char *)&str[i]);
	}
	if (str[i] == (char)c)
		return ((char *) &str[i]);
	return (0);
}
