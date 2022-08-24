def arithmetic_arranger(problems,bol=False):
    if len(problems)>5:
        return 'Error: Too many problems'

# String operation to get list of results: arranged_problems
    arranged_problems = []
    for problem in problems:
        op_pos = max(problem.find('+'),problem.find('-')) 
        if op_pos == -1:
            return 'Error: Operator must be \'+\' or \'-\''
        num1 = problem[:op_pos].strip()
        num2 = problem[op_pos+1:].strip()
        if num1.isdigit() and num2.isdigit():
            maxdigit = max(len(num1),len(num2))
            if maxdigit>4:
                return 'Error: Numbers cannot be more than four digits'
            arranged_problem = ' '*(maxdigit+2-len(num1))+num1+'\n'+problem[op_pos]+' '*(maxdigit+1-len(num2))+num2+'\n'+'-'*(maxdigit+2)+'\n'
            if bol:
                num3 = eval('int(num1) '+problem[op_pos]+' int(num2)')
                arranged_problem += ' '*(maxdigit+2-len(str(num3)))+str(num3)
            arranged_problems.append(arranged_problem)
        else:
            return 'Error: Numbers must only contain digits'


#Processing: arrage the results horizontally
    lines = []
    for i in range(4):
        line = []
        for arranged_problem in arranged_problems:
            line.append(arranged_problem.split('\n')[i])
        lines.append('    '.join(line))
    
    return '\n'.join(lines)

if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))