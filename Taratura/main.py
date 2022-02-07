# This is a sample Python script.
import Function
import random

if __name__ == '__main__':
    try:
        list=Function.open_data()
    except:
        list=[]
    if len(list)==0:
        index=int(0)
        list.append(index)
        v_min=Function.float_question("minimum velocity [RPM]:")
        list.append(v_min)
        v_max = Function.float_question("maximum velocity [RPM]:")
        list.append(v_max)
        reduction=Function.float_question("reduction motor/load:")
        list.append(reduction)
        division=Function.integer_question("number of division:")
        list.append(division)
        repetition=Function.integer_question("number of repetition of the ramp")
        list.append(repetition)
        is_disp_Hz=Function.digital_question("how do you want the velocity will be displaied?\nn-RPM\ny-Hz\n")
        list.append(is_disp_Hz)
    else:
        index=list[0]
        v_min=list[1]
        v_max=list[2]
        reduction=list[3]
        division=list[4]
        repetition=list[5]
        is_disp_Hz=list[6]
        Function.print_data_settings(list)
    dv=(v_max-v_min)/division
    if Function.digital_question("do you want to acquire some value?"):
        for i in range(index+1,division*2*repetition):
            ind = i % division
            if not int(i/division)%2:
                v_mot = int((v_min + ind * dv + random.randint(0,int(2*dv)) - dv) * reduction / 60)
                print("Set the motor speed at:\n"+str(v_mot))
                list.append([v_mot, Function.float_question("voltage value:")])
            else:
                v_mot = int((v_max - ind * dv + random.randint(0,int(2*dv)) - dv) * reduction / 60)
                print("Set the motor speed at:\n" + str(v_mot))
                list.append([v_mot, Function.float_question("voltage value:")])
            if not Function.digital_question("Do you want to continue?"):
                break
    list[0] = int(i)
    Function.save_data(list)