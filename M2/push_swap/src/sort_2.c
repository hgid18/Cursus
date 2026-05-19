/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_2.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 12:42:47 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/03/11 18:15:18 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_error(void)
{
	write(2, "Error\n", 6);
	exit(1);
}

int	find_position(t_stack *stack, int value)
{
	int	pos;

	pos = 0;
	while (stack)
	{
		if (stack->value == value)
			return (pos);
		pos++;
		stack = stack->next;
	}
	return (pos);
}

void	push_min(t_stack **a, t_stack **b)
{
	int	min;
	int	pos;

	min = get_min_value(*a);
	pos = find_position(*a, min);
	if (pos <= stack_size(*a) / 2)
	{
		while ((*a)->value != min)
			sort_rotate(a, "ra\n");
	}
	else
	{
		while ((*a)->value != min)
			sort_rrotate(a, "rra\n");
	}
	sort_push(a, b, "pb\n");
}

void	sort_two(t_stack **a)
{
	if ((*a)->value > (*a)->next->value)
		sort_swap(a, "sa\n");
}
