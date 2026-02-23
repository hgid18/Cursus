/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 10:37:55 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/02/23 12:41:07 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	normal_sort(t_list **a, t_list **b)
{
	int	size;

	size = lstsize(*a);
	if (size == 2)
	{
		if ((*a)->value > (*a)->next->value)
			sort_swap(a, "sa\n");
	}
	else if (size == 3)
	{
		if ((*a)->value > (*a)->next->value
			&& (*a)->value > lstlast(*a)->value)
			sort_rotate(a, "ra\n");
		else if ((*a)->next->value > (*a)->value
			&& (*a)->next->value > lstlast(*a)->value)
			sort_rrotate(a, "rra\n");
		if ((*a)->value > (*a)->next->value)
			sort_swap(a, "sa\n");
	}

}


