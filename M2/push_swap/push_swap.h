/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:42:58 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/02/23 12:42:12 by hgarcia2         ###   ########.fr       */
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
void	normal_sort(t_list **a, t_list **b);
void	turkish_sort(t_list **a, t_list **b);
int		get_min(t_list *stack);
int		get_max(t_list *stack);
int		get_position(t_list *stack, int value);
int		find_target_pos(t_list *a, int value);
int		calculate_cost(int pos_b, int pos_a, int size_a, int size_b);
void	move_cheapest(t_list **a, t_list **b);
void	do_move(t_list **a, t_list **b, int pos_a, int pos_b);
void	rotate_to_min(t_list **a);
void	normal_sort(t_list **a, t_list **b);

#endif
