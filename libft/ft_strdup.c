/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 16:23:56 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 16:26:52 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*strdup(const char *s)
{
	int		i;
	char	*str;

	i = 0;
	str = malloc(ft_strlen(s) * sizeof(char));
	while (str[++i])
		str[i] = s[i];
	return (str);
}
