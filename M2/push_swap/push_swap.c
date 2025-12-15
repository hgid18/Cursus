/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:45:02 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/12/11 15:12:06 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_swap(t_list **list, char *s)
{
	t_list	*first;
	t_list	*second;
	t_list	*third;

	if (!list || !*list || !(*list)->next)
		return ;
	first = *list;
	second = (*list)->next;
	third = second->next;
	*list = second;
	second->prev = NULL;
	second->next = first;
	first->next = third;
	first->prev = second;
	if (third)
		third->prev = first;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_rotate(t_list **list, char *s)
{
	t_list	*last;
	t_list	*first;

	if (!list || !*list || !(*list)->next)
		return ;
	first = *list;
	*list = first->next;
	last = *list;
	(*list)->prev = NULL;
	while (last->next)
		last = last->next;
	last->next = first;
	first->prev = last;
	first->next = NULL;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_rrotate(t_list **list, char *s)
{
	t_list	*last;
	t_list	*first;

	if (!list || !*list || !(*list)->next)
		return ;
	last = *list;
	while (last->next)
		last = last->next;
	if (last->prev)
		last->prev->next = NULL;
	last->prev = NULL;
	last->next = *list;
	(*list)->prev = last;
	*list = last;
	if (s)
		write(1, s, ft_strlen(s));
}

void	sort_push(t_list **a, t_list **b, char *s)
{
	t_list	*tmp;

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
