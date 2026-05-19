/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:45:02 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/03/11 18:15:05 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_swap(t_stack **stack, char *s)
{
	t_stack	*first;
	t_stack	*second;
	t_stack	*third;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = (*stack)->next;
	third = second->next;
	*stack = second;
	second->prev = NULL;
	second->next = first;
	first->next = third;
	first->prev = second;
	if (third)
		third->prev = first;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_rotate(t_stack **stack, char *s)
{
	t_stack	*last;
	t_stack	*first;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	*stack = first->next;
	last = *stack;
	(*stack)->prev = NULL;
	while (last->next)
		last = last->next;
	last->next = first;
	first->prev = last;
	first->next = NULL;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_rrotate(t_stack **stack, char *s)
{
	t_stack	*last;
	t_stack	*first;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	first = *stack;
	last = *stack;
	while (last->next)
		last = last->next;
	if (last->prev)
		last->prev->next = NULL;
	last->prev = NULL;
	last->next = first;
	first->prev = last;
	*stack = last;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_push(t_stack **a, t_stack **b, char *s)
{
	t_stack	*tmp;

	if (!a || !b || !*a)
		return ;
	tmp = *a;
	*a = (*a)->next;
	if (*a)
		(*a)->prev = NULL;
	tmp->next = *b;
	if (*b)
		(*b)->prev = tmp;
	tmp->prev = NULL;
	*b = tmp;
	if (s)
		write(1, s, ft_strlen(s));
}

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;

	if (argc < 2)
		return (0);
	a = parse_args(argc, argv);
	if (!a)
		ft_error();
	check_dups(&a);
	b = NULL;
	sort(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
