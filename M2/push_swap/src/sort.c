/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 10:37:55 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/02/24 12:51:52 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_error(void)
{
	write(1, "Error\n", 6);
	exit(1);
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
	{
		if ((*a)->value > (*a)->next->value)
			sort_swap(a, "sa\n");
	}
	else if (size == 3)
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
	else
		radix_sort(a, b);
}
