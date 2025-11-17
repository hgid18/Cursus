/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 18:12:32 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/17 12:53:23 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	i;
	char	*subs;

	i = 0;
	if (!s)
		return (NULL);
	if ((size_t)ft_strlen(s) <= start)
	{
		subs = malloc(1);
		subs[0] = '\0';
		return (subs);
	}
	subs = malloc((len + 1) * sizeof(char));
	if (!subs)
		return (NULL);
	while (i < len && s[start + i])
	{
		subs[i] = s[start + i];
		i++;
	}
	subs[i] = '\0';
	return (subs);
}
