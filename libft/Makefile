NAME := libft

CC := cc
CFLAGS := -Wall -Wextra -Werror

CFILES := ft_atoi.c ft_bzero.c ft_isalnum.c ft_isalpha.c \
			ft_isascii.c ft_isdigit.c ft_isprint.c ft_itoa.c \
			ft_memchr.c ft_memset.c ft_strchr.c ft_strlen.c \
			ft_strncmp.c ft_strrchr.c ft_tolower.c ft_toupper.c \
			ft_memcpy.c

OFILES := $(CFILES:.c=.o)

INCL = libft.h

all: $(NAME)

$(NAME): $(OFILES)
	$(CC) -I $(INCL) $(CFLAGS) $(OFILES) -o $(NAME)

clean:
	rm -f $(OFILES)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re