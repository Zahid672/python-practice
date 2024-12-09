def cpo_and_kwo(a, b, /, *, c, d):
    """can combine the two arguments in the same funcion.
    Any argument before the /, are positional-only, and any argument after the *, are keyword only."""
    
    print(a + b + c + d)
    
cpo_and_kwo(2, 3, c = 5, d = 10)