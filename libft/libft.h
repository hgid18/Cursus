/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 10:30:54 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/10 16:49:08 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H
# include <stdio.h>
# include <unistd.h>
# include <stdlib.h>

int		ft_isalpha(int c);
int		ft_toupper(int c);
int		ft_tolower(int c);
int		ft_isprint(int c);
int		ft_isdigit(int c);
int		ft_isalpha(int c);
int		ft_isalpha(int c);
int		ft_isalnum(int c);
int		ft_atoi(char *str);
int		ft_strncmp(char *s1, char *s2, int n);
int		ft_memcmp(const void *s1, const void *s2, size_t n);
size_t	ft_strlen(char *str);
size_t	strlcpy(char *dst, const char *src, size_t size);
size_t	strlcat(char *dst, const char *src, size_t size);
char	*ft_itoa(int nb);
char	*ft_strchr(char *str, int c);
char	*ft_strrchr(char *str, int c);
char	*strnstr(const char *big, const char *little, size_t len);
void	ft_bzero(void *s, size_t n);
void	ft_putchar_fd(char c, int fd);
void	ft_putstr_fd(char *str, int fd);
void	ft_putendl_fd(char *s, int fd);
void	ft_putnbr_fd(int n, int fd);
void	*calloc(size_t nmemb, size_t size);
void	*ft_memset(void *s, int c, size_t n);
void	*ft_memchr(const void *s, int c, size_t n);
void	*ft_memcpy(void *dest, const void *src, size_t n);
void	*ft_memmove(void *dest, const void *src, size_t n);

#endif