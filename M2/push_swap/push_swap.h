/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:42:58 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/01/28 11:11:21 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H
# include <unistd.h>
# include <stdlib.h>
# include <limits.h>

typedef struct s_list
{
	int				value;
	struct s_list	*next;
	struct s_list	*prev;
}	t_list;

t_list	*lstlast(t_list *lst);
void	ft_error(void);
int		check_dups(t_list *a);
int		lstsize(t_list *list);
size_t	ft_strlen(const char *str);
void	sort_swap(t_list **list, char *s);
void	sort_rotate(t_list **list, char *s);
void	sort_rrotate(t_list **list, char *s);
void	sort_push(t_list **a, t_list **b, char *s);

#endif
