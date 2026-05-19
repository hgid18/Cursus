/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 10:37:55 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/03/11 12:45:52 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	sort_three(t_stack **a)
{
	if ((*a)->value > (*a)->next->value
		&& (*a)->value > stack_last(*a)->value)
		sort_rotate(a, "ra\n");
	else if ((*a)->next->value > (*a)->value
		&& (*a)->next->value > stack_last(*a)->value)
		sort_rrotate(a, "rra\n");
	if ((*a)->value > (*a)->next->value)
		sort_swap(a, "sa\n");
}

static void	sort_four(t_stack **a, t_stack **b)
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
	sort_three(a);
	sort_push(b, a, "pa\n");
}

static void	sort_five(t_stack **a, t_stack **b)
{
	push_min(a, b);
	sort_four(a, b);
	sort_push(b, a, "pa\n");
}

static void	radix_sort(t_stack **a, t_stack **b)
{
	int	size;
	int	max_bits;
	int	bit;
	int	i;

	size = stack_size(*a);
	normalize_stack(a);
	max_bits = get_max_bits(*a);
	bit = 0;
	while (bit < max_bits)
	{
		i = 0;
		while (i < size)
		{
			if ((((*a)->value >> bit) & 1) == 0)
				sort_push(a, b, "pb\n");
			else
				sort_rotate(a, "ra\n");
			i++;
		}
		while (*b)
			sort_push(b, a, "pa\n");
		bit++;
	}
}

void	sort(t_stack **a, t_stack **b)
{
	int	size;

	if (!a || !*a || is_sorted(*a))
		return ;
	size = stack_size(*a);
	if (size == 2)
		sort_two(a);
	else if (size == 3)
		sort_three(a);
	else if (size == 4)
		sort_four(a, b);
	else if (size == 5)
		sort_five(a, b);
	else
		radix_sort(a, b);
}
