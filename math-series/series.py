def fibonacci(n):
    """
    :param n: term number in Fibonacci series
    :return: (n-1) + (n-2), where fibonacci(0) = 0 and fibonacci(1) = 1
    *this function uses recursion to find the return
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    """
    :param n: term number in Fibonacci series
    :return: (n-1) + (n-2), where fibonacci(0) = 0 and fibonacci(1) = 1
    *this function uses iteration to find the return
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        previous_term = 1
        two_terms_before_current = 0
        for _ in range(2, n + 1):
            current_term = previous_term + two_terms_before_current
            two_terms_before_current = previous_term
            previous_term = current_term


def lucas(n):
    """
    :param n: term number in Lucas series
    :return: (n-1) + (n-2), where lucas(0) = 2 and lucas(1) = 1
    *this function uses recursion to find the return, unless n is greater than 10
    """
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    elif n >= 10:
        previous_term = 1
        two_terms_before_current = 2
        for _ in range(2, n + 1):
            current_term = previous_term + two_terms_before_current
            two_terms_before_current = previous_term
            previous_term = current_term
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(term_num, starting_term=0, first_term=1):
    """
    :param term_num: term number in defined series
    :no optional params: will produce values from fibonacci series
    :optional params: 2 & 1 will produce values from lucas series, 0 & 1 will produce fibonacci anyway
    :return: (term_num-1) + (term_num-2), where starting_term = starting term & first_term = first term
    *if n>= 10, return will be iterative

    """
    if term_num <= 0:
        return starting_term
    elif term_num == 1:
        return first_term
    elif term_num >= 10:
        previous_term = first_term
        two_terms_before_current = starting_term
        for _ in range(2, term_num + 1):
            current_term = previous_term + two_terms_before_current
            two_terms_before_current = previous_term
            previous_term = current_term
    else:
        sum_series(term_num - 1) + sum_series(term_num - 2)
