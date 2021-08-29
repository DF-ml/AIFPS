
import WeaponSpacing
import WeaponTrajectory

def fun_WeaponChoose(WeaponName):
    # 功能：武器选择
    # 参数：武器名称
    # 返回：射击间隔，射击弹道
    if WeaponName == 'AKM':
        WSpacing = WeaponSpacing.AK
        WTrajectory = WeaponTrajectory.AK
    elif WeaponName == 'M416':
        WSpacing = 0.857
        WTrajectory=WeaponTrajectory.M416
    elif WeaponName == 'MK47':
        WSpacing = 0.1
    elif WeaponName == 'Groza':
        WSpacing = 0.1
    elif WeaponName == 'Bervl-M762':
        WSpacing = 0.1
    elif WeaponName == 'M16A4':
        WSpacing = 0.1
    elif WeaponName == 'AUG':
        WSpacing = 0.1
    elif WeaponName == 'SCAR-L':
        WSpacing = 0.1
    elif WeaponName == 'QBZ':
        WSpacing = 0.1
    elif WeaponName == 'G36C':
        WSpacing = 0.1
    # 精确射手步枪
    elif WeaponName == 'VSS':
        WSpacing = 0.1
    elif WeaponName == 'SKS':
        WSpacing = 0.1
    elif WeaponName == 'MK14':
        WSpacing = 0.1
    elif WeaponName == '自动装填步枪':
        WSpacing = 0.1
    elif WeaponName == 'Mini-14':
        WSpacing = 0.1
    elif WeaponName == 'QBU':
        WSpacing = 0.1
    # 狙击步枪
    elif WeaponName == '98K':
        WSpacing = 0.1
    elif WeaponName == 'M24':
        WSpacing = 0.1
    elif WeaponName == 'Win94':
        WSpacing = 0.1
    elif WeaponName == 'AWM':
        WSpacing = 0.1
    elif WeaponName == 'MosinNaqant':
        WSpacing = 0.1
    # 霰弹枪
    elif WeaponName == 'S686':
        WSpacing = 0.1
    elif WeaponName == 'S1897':
        WSpacing = 0.1
    elif WeaponName == '截短霰弹枪':
        WSpacing = 0.1
    elif WeaponName == 'S12K':
        WSpacing = 0.1
    elif WeaponName == 'DBS':
        WSpacing = 0.1
    # 冲锋枪
    elif WeaponName == 'Micor-UZI':
        WSpacing = 0.1
    elif WeaponName == 'UMP45':
        WSpacing = 0.1
    elif WeaponName == 'MP5K':
        WSpacing = 0.1
    elif WeaponName == 'PP-19':
        WSpacing = 0.1
    elif WeaponName == 'Vector':
        WSpacing = 0.1
    elif WeaponName == '汤姆逊':
        WSpacing = 0.1
    # 轻机枪
    elif WeaponName == 'M249':
        WSpacing = 0.1
    elif WeaponName == 'DP-28':
        WSpacing = 0.1
    elif WeaponName == 'MG3':
        WSpacing = 0.1
    # 手枪
    elif WeaponName == 'P18C':
        WSpacing = 0.1
    elif WeaponName == 'P92':
        WSpacing = 0.1
    elif WeaponName == 'R45':
        WSpacing = 0.1
    elif WeaponName == 'P1911':
        WSpacing = 0.1
    elif WeaponName == 'R1895':
        WSpacing = 0.1
    elif WeaponName == '蝎式手枪':
        WSpacing = 0.1
    elif WeaponName == 'DesertEaqle':
        WSpacing = 0.1
    else:
        print('没有找到武器')
        WSpacing = 0
        WTrajectory= ()
    return WSpacing,WTrajectory


# print('请输入武器:')
# WeaponName = input()
# Weapon = fun_WeaponChoose(WeaponName)
# Spacing = Weapon[0]                         #Spacing:float
# Trajectory = Weapon[1]                      #Trajectory:tuple
# print('武器：' + WeaponName)
# print('射击间隔：' + str(Spacing))
# print('射击弹道：')
# print(Trajectory)

