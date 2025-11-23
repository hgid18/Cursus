/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:23:56 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/14 13:30:34 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	int		i;
	char	*str;

	i = 0;
	str = malloc((ft_strlen(s) + 1) * sizeof(char));
	if (!str)
		return (NULL);
	str = ft_memcpy(str, s, ft_strlen(s) + 1);
	return (str);
}
