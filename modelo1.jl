using JuMP , HiGHS

model = Model("HiGHS")

@variable(model, x1 >=0)
@variable(model, x2 >=0)

@objective(model, Max, x1+2*x2)

@constraint (model,x1+3*x2<=6)
@constraint (model,7*x1+5*x2<=12)

optimize!(model)