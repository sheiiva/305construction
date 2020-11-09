############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#          Project : 305construction       #
#                                          #
############################################


NAME 	=	305construction

RM 		=	@rm -f
PRINT	=	@echo -e

SOURCES		=	sources/
TESTS		=	tests/


TESTS_SRC	=	$(TESTS)t_Usage.py					\
				$(TESTS)t_ArgumentManager.py		\
				$(TESTS)t_Pacman.py		\

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) -r __pycache__
	$(RM) -r $(SOURCES)__pycache__
	$(RM) -r $(SOURCES)sort/__pycache__
	$(RM) -r $(TESTS)__pycache__
	$(RM) -r $(TESTS)deps/__pycache__
	$(RM) .coverage
	$(RM) -r htmlcov
	$(RM) -r .pytest_cache

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARY\n"
	$(RM) $(NAME)

tests_run: fclean
	$(PRINT) "\nLET'S TEST:\n"
	@python3 -m pytest -v $(TESTS_SRC) --cov=$(SOURCES) --cov-report=html

re: fclean all

.PHONY: all clean fclean tests_run re