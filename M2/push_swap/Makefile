SRC_DIR			=	src
SRCS			=	push_swap.c sort.c sort_2.c utils.c utils2.c utils3.c

OBJ_DIR			=	$(SRC_DIR)/swap_objects
OBJS			=	$(addprefix $(OBJ_DIR)/, $(SRCS:.c=.o))

CC				=	cc
RM				=	rm -f
CFLAGS			=	-Wall -Wextra -Werror -I. -I$(SRC_DIR) -Ilibft

NAME			=	push_swap

LIBFT_DIR		=	libft
LIBFT			=	$(LIBFT_DIR)/libft.a

all:			$(NAME)

$(LIBFT):
				@make -C $(LIBFT_DIR)

$(OBJ_DIR):
				@mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
				$(CC) $(CFLAGS) -c $< -o $@

$(NAME):		$(LIBFT) $(OBJS)
				$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)

clean:
				$(RM) -r $(OBJ_DIR)
				@make -C $(LIBFT_DIR) clean

fclean:			clean
				$(RM) $(NAME)
				@make -C $(LIBFT_DIR) fclean

re:				fclean all

.PHONY:			all clean fclean re