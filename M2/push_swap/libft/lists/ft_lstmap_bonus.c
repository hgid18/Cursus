/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hgarcia2 <hgarcia2@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 12:00:47 by hgarcia2          #+#    #+#             */
/*   Updated: 2025/11/20 13:04:41 by hgarcia2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*lst2;
	t_list	*new;
	void	*str;

	lst2 = NULL;
	str = NULL;
	while (lst)
	{
		str = f(lst->content);
		if (!str)
		{
			ft_lstclear(&lst2, del);
			return (NULL);
		}
		new = ft_lstnew(str);
		if (!new)
		{
			ft_lstclear(&lst2, del);
			free (str);
			return (NULL);
		}
		ft_lstadd_back(&lst2, new);
		lst = lst->next;
	}
	return (lst2);
}
