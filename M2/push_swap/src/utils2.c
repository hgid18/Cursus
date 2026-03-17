/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils2.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/24 11:15:40 by hgarcia2          #+#    #+#             */
/*   Updated: 2026/02/25 09:45:11 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

long	ft_atol(const char *str)
{
	long	result;
	int		sign;

	result = 0;
	sign = 1;
	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -1;
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	return (result * sign);
}

int	is_valid_number(char *str)
{
	int		i;
	long	num;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (!ft_isdigit(str[i]))
			return (0);
		i++;
	}
	num = ft_atol(str);
	if (num > INT_MAX || num < INT_MIN)
		return (0);
	return (1);
}

static t_stack	*create_node(int value)
{
	t_stack	*node;

	node = (t_stack *)malloc(sizeof(t_stack));
	if (!node)
		return (NULL);
	node->value = value;
	node->next = NULL;
	node->prev = NULL;
	return (node);
}

static void	parse_string(char *str, t_stack **stack)
{
	char	**numbers;
	int		i;
	t_stack	*node;

	numbers = ft_split(str, ' ');
	if (!numbers)
		ft_error();
	i = 0;
	while (numbers[i])
	{
		if (!is_valid_number(numbers[i]))
		{
			while (numbers[i])
				free(numbers[i++]);
			free(numbers);
			free_stack(stack);
			ft_error();
		}
		node = create_node((int)ft_atol(numbers[i]));
		stack_add_back(stack, node);
		free(numbers[i]);
		i++;
	}
	free(numbers);
}

t_stack	*parse_args(int argc, char **argv)
{
	t_stack	*stack;
	int		i;

	stack = NULL;
	i = 0;
	while (++i < argc)
		parse_string(argv[i], &stack);
	return (stack);
}
