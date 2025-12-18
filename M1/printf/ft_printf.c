/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 18:15:40 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/12/16 13:51:20 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	types(char type, va_list args)
{
	if (type == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (type == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (type == 'd' || type == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (type == 'u')
		return (ft_putunbr(va_arg(args, unsigned int)));
	else if (type == 'p')
		return (ft_voidptr(va_arg(args, void *)));
	else if (type == 'x')
		return (ft_hexnbr(va_arg(args, unsigned int), type));
	else if (type == 'X')
		return (ft_hexnbr(va_arg(args, unsigned int), type));
	else if (type == '%')
		return (ft_putchar('%'));
	else
		return (0);
}

int	ft_printf(const char *s, ...)
{
	va_list	args;
	size_t	i;
	size_t	len;

	len = 0;
	i = -1;
	va_start (args, s);
	while (s[++i])
	{
		if (s[i] != '%')
			len += ft_putchar(s[i]);
		else
			len += types(s[++i], args);
	}
	va_end (args);
	return (len);
}

/*#include <stdio.h>
int main(void)
{
	int x = 0;
	int *p = &x;
	ft_printf("%c\n", 'a');
	printf("%c\n", 'a');
	ft_printf("%s\n", "pepe");
	printf("%s\n", "pepe");
	ft_printf("%d\n", 13);
	printf("%d\n", 13);
	ft_printf("%p\n", p);
	printf("%p\n", p);
	ft_printf("%i\n", -14);
	printf("%i\n", -14);
	ft_printf("%u\n", 15);
	printf("%u\n", 15);
	ft_printf("%x\n", 'd');
	printf("%x\n", 'd');
	ft_printf("%X\n", 'D');
	printf("%X\n", 'D');
	ft_printf("%%\n");
	printf("%%\n");
}*/
