from Solver import ExpressionSolver


if __name__ == '__main__':
    solver = ExpressionSolver()
    solver.setStreamerFunction(lambda data: print(f"\t\t=> {data}"))
    
    print('Enter `Q` or `q` to exit.')
    while True:
        n = input("Enter an expression >> ").strip()
        
        if n.lower() == 'q':
            break
        
        Steps = None
        Solution = solver.solve(
            expression = n, 
            steps_return = solver.StepsReturnAsStream
        )
        
        if len(Solution) > 1:
            # Steps = Solution[1]
            Solution = Solution[0]
            
        print(f'{Solution = }')
        # if Steps: print(f'{Steps = }')

