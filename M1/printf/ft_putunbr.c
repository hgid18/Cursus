/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putunbr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 18:59:57 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/19 15:51:12 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putunbr(unsigned int n)
{
	size_t	len;

	len = 0;
	if (n == 0)
		return (ft_putchar('0'));
	if (n >= 10)
		len += ft_putnbr(n / 10);
	len += ft_putchar((n % 10) + '0');
	return (len);
}
