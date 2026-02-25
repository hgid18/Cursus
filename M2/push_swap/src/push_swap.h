/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:42:58 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/02/24 12:38:24 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H
# include "../libft/libft.h"
# include <limits.h>

typedef struct s_stack
{
	int				value;
	struct s_stack	*next;
	struct s_stack	*prev;
}	t_stack;

void	ft_error(void);
int		check_dups(t_stack **a);
t_stack	*stack_last(t_stack *stack);
int		stack_size(t_stack *stack);
void	sort_swap(t_stack **stack, char *s);
void	sort_rotate(t_stack **stack, char *s);
void	sort_rrotate(t_stack **stack, char *s);
void	sort_push(t_stack **a, t_stack **b, char *s);
void	sort(t_stack **a, t_stack **b);

// Parsing and initialization
t_stack	*parse_args(int argc, char **argv);
void	stack_add_back(t_stack **stack, t_stack *new);
void	free_stack(t_stack **stack);
int		is_valid_number(char *str);
long	ft_atol(const char *str);

// Radix Sort utilities
int		is_sorted(t_stack *stack);
void	normalize_stack(t_stack **stack);
int		get_max_bits(t_stack *stack);
int		get_min_value(t_stack *stack);
int		get_max_value(t_stack *stack);

#endif
