/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 11:55:12 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 15:58:45 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	int_len(long int nb)
{
	int	i;

	i = 0;
	if (nb <= 0)
		i++;
	if (nb < 0)
		nb *= -1;
	while (nb > 0)
	{
		nb = nb / 10;
		i++;
	}
	return (i);
}

char	*ft_itoa(int nb)
{
	long int	n;
	char		*str;
	int			l;

	n = nb;
	l = int_len(n);
	str = malloc((l + 1) * sizeof(char));
	if (!str)
		return (0);
	str[l] = '\0';
	if (n < 0)
	{
		str[0] = '-';
		n = n * -1;
	}
	if (n == 0)
		str[0] = '0';
	while (n > 0)
	{
		str[--l] = n % 10 + '0';
		n = n / 10;
	}
	return (str);
}

/*#include <stdio.h>
int main()
{
	printf("%s",itoa(-23475234));
}*/
