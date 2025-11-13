using JuMP , HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x[1:8] >= 0, Int)

@objective(model, Min, sum(x[i] for i=1:8))

@constraint(model, 10*x[1] + 2*x[5] + 3*x[8] >= 10000)
@constraint(model, 7*x[2 ]+ x[5] + 2*x[6] + x[7] + x[8]>= 7000)
@constraint(model, 5*x[3] + 3*x[5] + 2*x[6] + x[7] + x[8] >= 5000)
@constraint(model, 3*x[4] + x[6] + 2*x[7] + x[8] >= 2000)

print(model)

optimize!(model)

if termination_status(model) == MOI.OPTIMAL
    println("Solução ótima encontrada:")
    println("Valor da Função Objetivo: ", objective_value(model))
    println("Valores de x: ", value.(x))
else
    println("Solução ótima não encontrada.")
end
