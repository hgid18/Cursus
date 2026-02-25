SRCS			=	push_swap.c sort.c utils.c utils2.c utils3.c

OBJS			=	$(SRCS:.c=.o)

CC				=	cc
RM				=	rm -f
CFLAGS			=	-Wall -Wextra -Werror -I. -I../libft

NAME			=	push_swap

LIBFT_DIR		=	../libft
LIBFT			=	$(LIBFT_DIR)/libft.a

all:			$(NAME)

$(LIBFT):
				@make -C $(LIBFT_DIR)

%.o: %.c
				$(CC) $(CFLAGS) -c $< -o $@

$(NAME):		$(LIBFT) $(OBJS)
				$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)

clean:
				$(RM) $(OBJS)
				@make -C $(LIBFT_DIR) clean

fclean:			clean
				$(RM) $(NAME)
				@make -C $(LIBFT_DIR) fclean

re:				fclean all

.PHONY:			all clean fclean re