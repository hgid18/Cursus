/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 14:59:08 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/19 16:52:44 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int	ft_voidptr(void *a);
int	ft_putchar(char c);
int	ft_putstr(char *str);
int	ft_hexnbr(unsigned long n, int x);
int	ft_putnbr(int n);
int	ft_putunbr(unsigned int n);
int	ft_printf(const char *s, ...);

#endif
