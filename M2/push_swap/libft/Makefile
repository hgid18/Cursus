SRCS    =   is/ft_isalpha.c is/ft_isdigit.c is/ft_isalnum.c is/ft_isascii.c is/ft_isprint.c \
			mem/ft_memset.c mem/ft_memcpy.c mem/ft_memmove.c mem/ft_memchr.c mem/ft_memcmp.c \
			mem/ft_calloc.c mem/ft_bzero.c \
			fd/ft_putchar_fd.c fd/ft_putstr_fd.c fd/ft_putendl_fd.c fd/ft_putnbr_fd.c \
			convert/ft_toupper.c convert/ft_tolower.c convert/ft_atoi.c convert/ft_itoa.c \
			strs/ft_strlcpy.c strs/ft_strlcat.c strs/ft_strchr.c strs/ft_strrchr.c \
			strs/ft_strlen.c strs/ft_strncmp.c strs/ft_strnstr.c strs/ft_strdup.c \
			strs/ft_substr.c strs/ft_strjoin.c strs/ft_strtrim.c strs/ft_strmapi.c \
			strs/ft_striteri.c  strs/ft_split.c

BONUS       =   lists/ft_lstnew_bonus.c lists/ft_lstadd_front_bonus.c lists/ft_lstsize_bonus.c \
				lists/ft_lstlast_bonus.c lists/ft_lstadd_back_bonus.c lists/ft_lstdelone_bonus.c \
				lists/ft_lstclear_bonus.c lists/ft_lstiter_bonus.c lists/ft_lstmap_bonus.c

OBJDIR      =   objects

OBJS        =   $(patsubst %.c,$(OBJDIR)/%.o,$(notdir $(SRCS)))
BONUS_OBJS  =   $(patsubst %.c,$(OBJDIR)/%.o,$(notdir $(BONUS)))

CC          =   cc
RM          =   rm -f
CFLAGS      =   -Wall -Wextra -Werror -I.

NAME        =   libft.a

all: $(NAME)

$(OBJDIR)/%.o:
	mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -c $(filter %/$*.c, $(SRCS) $(BONUS)) -o $@

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

bonus: $(BONUS_OBJS)
	ar rcs $(NAME) $(OBJS) $(BONUS_OBJS)

clean:
	rm -rf $(OBJDIR)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re bonus

