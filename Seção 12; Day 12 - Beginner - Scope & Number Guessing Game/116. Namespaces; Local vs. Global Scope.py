###########################################################################################################

# Local Scope --> Geralmente encontrado dentro de funções e for loops
def drink_potion():
    potion_strength = 2
    print(potion_strength)

# A variável potion_strength está dentro da função drink_potion(), logo, é uma variável de escopo local.
drink_potion()
# Por ser uma variável local, não conseguimos obter seu valor fora da função. 
print(potion_strength)

###########################################################################################################

# Global Scope --> São variáveis que estão no "top level" do código. Podem ser usadas em qualquer lugar a qualquer momento
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

# Por ser uma variável de escopo global, a função consegue printar o valor da variável
drink_potion()
# E como dito acima, por ser uma variável global, podemos obter seu valor a qualquer momento
print(player_health)

###########################################################################################################

# Sempre ao dar nomes a funções e variáveis, devemos sempre ter em mente a sua indentação
# Por exemplo, uma função com uma variável dentro: Sua variável é uma variável de escopo local
# Porém, também poderia ser uma função dentro de função, logo, sua variável seria de escopo local dentro da função e a função de dentro seria de escopo local da função mais externa

def outter_function():
    def inner_function():
        local_scope_inner_function_variable = 30
        print(local_scope_inner_function_variable)
    inner_function()
    local_scope_outter_function_variable = 100
    print(local_scope_outter_function_variable)

# Neste caso, podemos apenas chamar a função mais externa deste bloco de código, pois sua função interna é de escopo local da função externa
outter_function()
# Como dito acima, a função inner_function() é uma função interna da função outter_function(), o que significa que é uma função de escopo local
inner_function()
# Ambas as variáveis são de escopo local da função interna e externa respectivamente. Não podem ser chamadas fora de suas respectivas funções
print(local_scope_inner_function_variable)
print(local_scope_outter_function_variable)

###########################################################################################################

# Block Scope --> Não há em Python. (Variáveis block scope são criadas dentro de blocos como if, while etc, porém não existem em Python.)