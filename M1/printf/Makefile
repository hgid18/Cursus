SRCS			=	ft_putchar.c ft_putnbr.c ft_putstr.c ft_printf.c \
					ft_voidptr.c ft_hexnbr.c ft_putunbr.c 

OBJS			=	$(SRCS:.c=.o)

CC			=	cc
RM			=	rm -f
CFLAGS			=	-Wall -Wextra -Werror -I.

NAME			=	libftprintf.a

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

all:			$(NAME)

$(NAME):		$(OBJS)
				ar rcs $(NAME) $(OBJS)

clean:
				$(RM) $(OBJS) $(BONUS_OBJS)

fclean:			clean
				$(RM) $(NAME)

re:			fclean $(NAME)

bonus:			$(OBJS) $(BONUS_OBJS)
				ar rcs $(NAME) $(OBJS) $(BONUS_OBJS)

.PHONY:			all clean fclean re bonus