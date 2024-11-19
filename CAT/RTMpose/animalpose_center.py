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
        0:dict( name='101', id=0, color=[0, 255, 0], type='upper', swap='201'),
        1:dict( name='102', id=1, color=[0, 255, 0], type='upper', swap='202'),
        2:dict( name='103', id=2, color=[0, 255, 0], type='upper', swap='203'),
        3:dict( name='104', id=3, color=[0, 255, 0], type='upper', swap='204'),

        4:dict( name='201', id=4, color=[0, 0, 255], type='lower', swap='101'),
        5:dict( name='202', id=5, color=[0, 0, 255], type='lower', swap='102'),
        6:dict( name='203', id=6, color=[0, 0, 255], type='lower', swap='103'),
        7:dict( name='204', id=7, color=[0, 0, 255], type='lower', swap='104'),

        8:dict( name='301', id=0, color=[255, 0, 0], type='upper', swap='401'),
        9:dict( name='302', id=1, color=[255, 0, 0], type='upper', swap='402'),
        10:dict( name='303', id=2, color=[255, 0, 0], type='upper', swap='403'),
        11:dict( name='304', id=3, color=[255, 0, 0], type='upper', swap='404'),

        12:dict( name='401', id=0, color=[0, 255, 255], type='lower', swap='301'),
        13:dict( name='402', id=1, color=[0, 255, 255], type='lower', swap='302'),
        14:dict( name='403', id=2, color=[0, 255, 255], type='lower', swap='303'),
        15:dict( name='404', id=3, color=[0, 255, 255], type='lower', swap='304'),
    },
        skeleton_info={
        0: dict(link=('101', '102'), id=0, color=[0, 255, 0]),
        1: dict(link=('102', '103'), id=1, color=[0, 255, 0]),
        2: dict(link=('103', '104'), id=2, color=[0, 255, 0]),

        3: dict(link=('201', '202'), id=3, color=[0, 0, 255]),
        4: dict(link=('202', '203'), id=4, color=[0, 0, 255]),
        5: dict(link=('203', '204'), id=5, color=[0, 0, 255]),

        6: dict(link=('301', '302'), id=6, color=[255, 0, 0]),
        7: dict(link=('302', '303'), id=7, color=[255, 0, 0]),
        8: dict(link=('303', '304'), id=8, color=[255, 0, 0]),

        9: dict(link=('401', '402'), id=9, color=[0, 255, 255]),
        10: dict(link=('402', '403'), id=10, color=[0, 255, 255]),
        11: dict(link=('403', '404'), id=11, color=[0, 255, 255]),

        12: dict(link=('101', '201'), id=12, color=[0, 128, 128]),
        13: dict(link=('301', '401'), id=13, color=[255, 255, 255]),
    },
    
   joint_weights=[
       1., 1., 1., 1., 1., 1., 1., 1., 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2
   ],

     sigmas=[
         0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 
         0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050, 0.050
     ]

)