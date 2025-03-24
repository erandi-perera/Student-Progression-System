# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20518664 
# Date: 10.12.1023

from graphics import *
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
total_inputs=0
outcome_list=[]

print('1.Student\n2.Staff')
option=int(input('Select a option: '))
if option==1:                                  # Allowing students to predict their progression outcome
    while True:
        while True:                                                                  # Checking the validation
            try:
                pass_credit=int(input('Please enter your credits at pass:'))
                while pass_credit not in range(0,121,20):
                    print('Out of range')
                    pass_credit=int(input('Please enter your credits at pass:'))
                break
            except ValueError:
                print('Integer required')
        while True:
            try:
                defer_credit=int(input('Please enter your credit at defer:'))
                while defer_credit not in range(0,121,20):
                    print('Out of range')
                    defer_credit=int(input('Please enter your credit at defer:'))
                break
            except ValueError:
                print('Integer required')
        while True:
            try:
                fail_credit=int(input('Please enter your credit at fail:'))
                while fail_credit not in range(0,121,20):
                    print('Out of range')
                    fail_credit=int(input('Please enter your credit at fail:'))
                break
            except ValueError:
                print('Integer required')

        total_credit=pass_credit+defer_credit+fail_credit
        if total_credit==120:
            if pass_credit==120:                                    # Checking if predicts Outcomes (conditions) correctly
                print('Progress')
            elif pass_credit==100:
                print('Progress(module trailer)')
            elif fail_credit>=80:
                print('Exclude')
            else:
                print('Module retriever')
            break
        else:
            print('Total incorrect')
        
elif option==2:                                     # Allowing a staff member to predict progression outcomes
    while True:
        while True:                                                             # Checking the validation
            try:
                pass_credit=int(input('Enter your total PASS credits:'))
                while pass_credit not in range(0,121,20):
                    print('Out of range')
                    pass_credit=int(input('Enter your total PASS credits:'))
                break
            except ValueError:
                print('Integer required')
        while True:
            try:
                defer_credit=int(input('Enter your total DEFER credits:'))
                while defer_credit not in range(0,121,20):
                    print('Out of range')
                    defer_credit=int(input('Enter your total DEFER credits:'))
                break
            except ValueError:
                print('Integer required')
        while True:
            try:
                fail_credit=int(input('Enter your total FAIL credits:'))
                while fail_credit not in range(0,121,20):
                    print('Out of range')
                    fail_credit=int(input('Enter your total FAIL credits:'))
                break
            except ValueError:
                print('Integer required')

        total_credit=pass_credit+defer_credit+fail_credit
        if total_credit==120:                        #confirming the total is correct
            total_inputs+=1
                    
            if pass_credit==120:                      # Checking if predicts Outcomes (conditions) correctly 
                outcome='Progress'
                print('Progress')
                outcome_list.append(outcome)
                progress_count+=1
            elif pass_credit==100:
                outcome='Progress(module trailer)'
                outcome_list.append(outcome)
                print(outcome)
                trailer_count+=1
            elif fail_credit>=80:
                outcome='Exclude'
                outcome_list.append(outcome)
                print(outcome)
                exclude_count+=1
            else:
                outcome='Module retriever'
                outcome_list.append(outcome)
                print(outcome)
                retriever_count+=1
            outcome_list.append(pass_credit)                                         # Appending credits to outcome_list
            outcome_list.append(defer_credit)
            outcome_list.append(fail_credit)
            print('Would you like to enter another set of data?')                            
            entry=str(input("Enter 'y' for yes or 'q' to quit and view results: "))
                        
            if entry=='q':
                def drawHistrogram():                                     # Histrogram
                    program = GraphWin('Histogram', 600, 300)
                                    
                    def createText(position,text,size,style,color):
                        text=Text(position,text)
                        text.setSize(size)
                        text.setStyle(style)
                        text.setTextColor(color)
                        text.draw(program)
                        return text
                    my_heading=createText(Point(150,30),'Histogram Results',14,'bold','black')
                    aLine = Line(Point(50,240), Point(550,240))
                    aLine.draw(program)
                                    
                    def createRectangle(Point1,Point2,color):
                        rectangle = Rectangle(Point1, Point2)
                        rectangle.setFill(color)
                        rectangle.draw(program)
                        return rectangle
                    Rectangle1 =createRectangle(Point(70,240), Point(150,240-(progress_count*6)),'lime')
                    Rectangle2 =createRectangle(Point(170,240), Point(250,240-(trailer_count*6)),'green')
                    Rectangle3 =createRectangle(Point(270,240), Point(350,240-(retriever_count*6)),'olive')
                    Rectangle4 =createRectangle(Point(370,240), Point(450,240-(exclude_count*6)),'pink')
                                    
                    text1 = createText(Point(110,260), 'Progress',10,'bold','gray')
                    text2 = createText(Point(210,260), 'Trailer',10,'bold','gray')
                    text3 = createText(Point(310,260), 'Retriever',10,'bold','gray')
                    text4 = createText(Point(410,260), 'Excluded',10,'bold','gray')
                                    
                    number1 = createText(Point(110,220-(progress_count*6)),progress_count,10,'bold','gray')
                    number2 = createText(Point(210,220-(trailer_count*6)),trailer_count,10,'bold','gray')
                    number3 = createText(Point(310,220-(retriever_count*6)),retriever_count,10,'bold','gray')
                    number4 = createText(Point(410,220-(exclude_count*6)),exclude_count,10,'bold','gray')
                                    
                    last_text1 = createText(Point(60,280),total_inputs,12,'bold','gray')
                    last_text2 = createText(Point(150,280),'outcomes in total',12,'bold','gray')
                                    
                    program.getMouse()
                    program.close()
                drawHistrogram()
                
                #Part 2 - List (extension)
                for i in range(0,len(outcome_list),4):
                    print(outcome_list[i],'-',outcome_list[i+1],',',outcome_list[i+2],',',outcome_list[i+3])
                    
                #Part 3 - Text File (extension)
                f = open('results.txt', 'w') 
                for i in range(0,len(outcome_list),4):
                    if outcome_list[i]=='Progress':
                        f.write(f'Progress- {outcome_list[i+1],outcome_list[i+2],outcome_list[i+3]}\n')
                    if outcome_list[i]=='Progress(module trailer)':
                        f.write(f'Progress(module trailer)- {outcome_list[i+1],outcome_list[i+2],outcome_list[i+3]}\n')
                    if outcome_list[i]=='Module retriever':
                        f.write(f'Module retriever- {outcome_list[i+1],outcome_list[i+2],outcome_list[i+3]}\n')
                    if outcome_list[i]=='Exclude':
                        f.write(f'Exclude- {outcome_list[i+1],outcome_list[i+2],outcome_list[i+3]}\n')
                f.close()
                break    
            elif entry=='y':                                         # Program loops to predicts progression outcomes for multiple inputs
                continue
        else:
            print('Total incorrect')
