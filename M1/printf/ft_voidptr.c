/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_voidptr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 19:39:25 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/19 16:50:41 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_voidptr(void *a)
{
	unsigned long	ua;
	int				len;

	if (!a)
		return (ft_putstr("(nil)"));
	len = 0;
	ua = (unsigned long) a;
	len += ft_putstr("0x");
	len += ft_hexnbr(ua, 'x');
	return (len);
}
