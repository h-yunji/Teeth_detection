dataset_info = dict(
    dataset_name='animalpose',
    paper_info=dict(
        author='Cao, Jinkun and Tang, Hongyang and Fang, Hao-Shu and '
        'Shen, Xiaoyong and Lu, Cewu and Tai, Yu-Wing',
        title='Cross-Domain Adaptation for Animal Pose Estimation',
        container='The IEEE International Conference on '
        'Computer Vision (ICCV)',
        year='2019',
        homepage='https://sites.google.com/view/animal-pose/',
    ),
    keypoint_info={
        0:dict( name='U1', id=0, color=[0, 255, 0], type='upper'),
        1:dict( name='U2', id=1, color=[0, 255, 0], type='upper'),
        2:dict( name='U3', id=2, color=[0, 255, 0], type='upper'),
        3:dict( name='U4', id=3, color=[0, 255, 0], type='upper'),

        4:dict( name='U5', id=4, color=[0, 0, 255], type='upper'),
        5:dict( name='U6', id=5, color=[0, 0, 255], type='upper'),
        6:dict( name='U7', id=6, color=[0, 0, 255], type='upper'),
        7:dict( name='U8', id=7, color=[0, 0, 255], type='upper'),

        8:dict( name='D1', id=0, color=[255, 0, 0], type='lower'),
        9:dict( name='D2', id=1, color=[255, 0, 0], type='lower'),
        10:dict( name='D3', id=2, color=[255, 0, 0], type='lower'),
        11:dict( name='D4', id=3, color=[255, 0, 0], type='lower'),

        12:dict( name='D5', id=4, color=[0, 255, 255], type='lower'),
        13:dict( name='D6', id=5, color=[0, 255, 255], type='lower'),
        14:dict( name='D7', id=6, color=[0, 255, 255], type='lower'),
        15:dict( name='D8', id=7, color=[0, 255, 255], type='lower'),
        16:dict( name='D9', id=8, color=[0, 255, 255], type='lower')
    },
        skeleton_info = {
        0: dict(link=('U1', 'U2'), id=0, color=[0, 255, 0]),
        1: dict(link=('U2', 'U3'), id=1, color=[0, 255, 0]),
        2: dict(link=('U3', 'U4'), id=2, color=[0, 255, 0]),
            
        3: dict(link=('U4', 'U5'), id=3, color=[0, 0, 255]),
        4: dict(link=('U5', 'U6'), id=4, color=[0, 0, 255]),
        5: dict(link=('U6', 'U7'), id=5, color=[0, 0, 255]),
            
        6: dict(link=('U7', 'U8'), id=6, color=[255, 0, 0]),
        7: dict(link=('D1', 'D2'), id=7, color=[255, 0, 0]),
        8: dict(link=('D2', 'D3'), id=8, color=[255, 0, 0]),
            
        9: dict(link=('D3', 'D4'), id=9, color=[0, 255, 255]),
        10: dict(link=('D4', 'D5'), id=10, color=[0, 255, 255]),
        11: dict(link=('D5', 'D6'), id=11, color=[0, 255, 255]),
            
        12: dict(link=('D6', 'D7'), id=12, color=[0, 128, 128]),
            
        13: dict(link=('D7', 'D8'), id=13, color=[255, 255, 255]),
        14: dict(link=('D8', 'D9'), id=14, color=[255, 255, 255]),
    },
    
   joint_weights=[
       1., 1., 1., 1., 1., 1., 1., 1., 
       1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2
   ],

     sigmas=[
         0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 
         0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050
     ]

)