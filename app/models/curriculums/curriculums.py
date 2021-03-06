from app.models.curriculums._template import Curriculum


CS = Curriculum(**{
    'intros': set([
        'csc 400', 'csc 401', 'csc 402',
        'csc 403', 'csc 406', 'csc 407']),
    'foundations': set([
        'csc 421', 'csc 435', 'csc 447',
        'csc 453', 'se 450']),
    'softDevs': set([
        'csc 436', 'csc 438', 'csc 439',
        'csc 443', 'csc 448', 'csc 461',
        'csc 462', 'csc 471', 'csc 472',
        'csc 475', 'csc 534', 'csc 536',
        'csc 540', 'csc 548', 'csc 549',
        'csc 551', 'csc 552', 'csc 553',
        'csc 595', 'cns 450', 'gam 690',
        'gam 691', 'hci 441', 'se 441',
        'se 452', 'se 459', 'se 525',
        'se 526', 'se 554', 'se 560',
        'se 491', 'se 591', 'tdc 478',
        'tdc 484', 'tdc 568']),
    'theorys': set([
        'csc 431', 'csc 440', 'csc 444_no',
        'csc 489', 'csc 503_no', 'csc 521',
        'csc 525', 'csc 531_no', 'csc 535_no',
        'csc 547_no', 'csc 557_no', 'csc 580_no',
        'csc 591_no', 'se 553_no']),
    'dataScis': set([
        'csc 423', 'csc 424', 'csc 433',
        'csc 465', 'csc 478', 'csc 481',
        'csc 482', 'csc 495', 'csc 529',
        'csc 555', 'csc 575', 'csc 578',
        'csc 594', 'csc 598', 'csc 672']),
    'databases': set([
        'csc 433', 'csc 452', 'csc 454',
        'csc 478', 'csc 529', 'csc 543',
        'csc 549', 'csc 551', 'csc 553',
        'csc 554', 'csc 555', 'csc 575',
        'csc 589']),
    'ais': set([
        'csc 457', 'csc 458', 'csc 478',
        'csc 480', 'csc 481', 'csc 482',
        'csc 495', 'csc 528', 'csc 529',
        'csc 538', 'csc 575', 'csc 576',
        'csc 577', 'csc 578', 'csc 583',
        'csc 587', 'csc 592', 'csc 594',
        'ect 584', 'geo 441', 'geo 442',
        'is 467']),
    'softEngs': set([
        'se 430', 'se 433', 'se 441',
        'csc 452', 'se 453', 'se 456',
        'se 457', 'se 459', 'se 475',
        'se 477', 'se 480', 'se 482',
        'se 491', 'se 525', 'se 526',
        'se 529', 'se 533', 'se 546',
        'se 549', 'se 554', 'se 556',
        'se 560', 'se 579', 'se 581',
        'se 582', 'se 591']),
    'gameRTSys': set([
        'se 461', 'csc 462', 'csc 486',
        'csc 588', 'gam 425', 'gam 450',
        'gam 453', 'gam 470', 'gam 475',
        'gam 476', 'gam 486', 'gam 575',
        'gam 576', 'gam 690', 'gam 691',
        'gph 436', 'gph 469', 'gph 570',
        'gph 572', 'gph 580', 'se 456']),
    'humCompInts': set([
        'csc 436', 'csc 438', 'csc 465',
        'csc 471', 'csc 472', 'csc 491',
        'csc 492', 'hci 440', 'hci 441',
        'hci 430', 'hci 454']),
    'majElects': set([
        'geo 441', 'geo 442', 'csc 444',
        'gam 450', 'csc 554', 'gam 691',
        'gam 690', 'csc 557', 'gam 453',
        'csc 672', 'csc 576', 'cns 450',
        'csc 575', 'csc 578', 'csc 531',
        'se 582', 'se 581', 'csc 436',
        'csc 478', 'csc 433', 'hci 441',
        'hci 440', 'csc 536', 'csc 472',
        'csc 471', 'csc 535', 'csc 439',
        'csc 438', 'se 525', 'se 453',
        'se 452', 'se 457', 'se 456',
        'se 459', 'se 556', 'se 553',
        'hci 454', 'tdc 568', 'se 526',
        'csc 491', 'gph 570', 'se 533',
        'gph 572', 'se 554', 'csc 589',
        'csc 588', 'csc 587', 'csc 583',
        'csc 580', 'csc 424', 'csc 549',
        'csc 548', 'csc 503', 'csc 423',
        'csc 543', 'csc 461', 'csc 462',
        'csc 540', 'csc 547', 'csc 465',
        'se 549', 'se 482', 'se 546',
        'csc 577', 'gam 476', 'gam 475',
        'se 529', 'gph 580', 'gam 470',
        'gam 576', 'tdc 478', 'gam 575',
        'gph 436', 'csc 454', 'csc 457',
        'csc 598', 'se 480', 'is 467',
        'csc 594', 'csc 595', 'csc 492',
        'csc 495', 'csc 458', 'csc 592',
        'csc 452', 'csc 551', 'csc 552',
        'csc 553', 'gam 486', 'csc 555',
        'csc 475', 'csc 591', 'se 433',
        'se 430', 'gph 469', 'se 477',
        'se 475', 'csc 486', 'csc 482',
        'csc 480', 'csc 481', 'gam 425',
        'csc 489', 'csc 443', 'csc 440',
        'se 491', 'ect 584', 'tdc 484',
        'csc 448', 'csc 521', 'csc 525',
        'csc 538', 'se 579', 'se 591',
        'csc 529', 'csc 528', 'hci 430',
        'se 461', 'se 560', 'se 441',
        'csc 431', 'csc 534']),
    'gradReqs': [6, 5, 8, 0, 0, 4, 0]
# Indexes correspond to the number of intro, foundation, major electives, open electives, capstones, courses \
# from a single concentration required for graduation, and advanced_courses
})


IS_BA_SA = Curriculum(**{
    'foundations': set([
        'is 421', 'csc 451', 'is 422',
        'is 430']),
    'advCourses': set([
        'cns 440', 'is 435', 'is 485',
        'is 535', 'is 560']),
    'openElects': set([
        'cns 450', 'cns 455',
        'cns 466', 'cns 477', 'cns 488',
        'cns 489', 'cns 490', 'cns 533',
        'cns 587', 'cns 594', 'cns 597',
        'cns 599', 'csc 421', 'csc 426',
        'csc 431', 'csc 435', 'csc 436',
        'csc 438', 'csc 439', 'csc 440',
        'csc 443', 'csc 444', 'csc 447',
        'csc 448', 'csc 452',
        'csc 453', 'csc 454', 'csc 457',
        'csc 458', 'csc 461', 'csc 462',
        'csc 471', 'csc 472', 'csc 475',
        'csc 480', 'csc 481', 'csc 482',
        'csc 485', 'csc 486', 'csc 489',
        'csc 491', 'csc 492', 'csc 500',
        'csc 503', 'csc 521', 'csc 525',
        'csc 528', 'csc 531', 'csc 534',
        'csc 535', 'csc 536', 'csc 538',
        'csc 540', 'csc 543', 'csc 547',
        'csc 548', 'csc 549', 'csc 550',
        'csc 551', 'csc 552', 'csc 553',
        'csc 554', 'csc 555', 'csc 557',
        'csc 559', 'csc 575', 'csc 576',
        'csc 577', 'csc 578', 'csc 580',
        'csc 583', 'csc 587', 'csc 588',
        'csc 589', 'csc 590', 'csc 591',
        'csc 592', 'csc 594', 'csc 595',
        'csc 598', 'csc 599', 'csc 601',
        'csc 690', 'csc 695', 'csc 696',
        'csc 697', 'csc 698', 'csc 699',
        'ect 436', 'ect 455',
        'ect 481', 'ect 556',
        'ect 565', 'ect 582', 'ect 583',
        'ect 586', 'ect 587', 'ect 589',
        'ect 596', 'ect 690', 'ect 696',
        'ect 698', 'gam 424', 'gam 425',
        'gam 426', 'gam 427', 'gam 428',
        'gam 430', 'gam 440', 'gam 450',
        'gam 451', 'gam 453', 'gam 462',
        'gam 470', 'gam 475', 'gam 476',
        'gam 486', 'gam 491', 'gam 499',
        'gam 520', 'gam 530', 'gam 540',
        'gam 550', 'gam 575', 'gam 576',
        'gam 594', 'gam 597', 'gam 598',
        'gam 599', 'gam 600', 'gam 690',
        'gam 691', 'gam 695', 'gph 425',
        'gph 436', 'gph 438', 'gph 448',
        'gph 450', 'gph 469', 'gph 487',
        'gph 536', 'gph 538', 'gph 539',
        'gph 540', 'gph 541', 'gph 560',
        'gph 565', 'gph 570', 'gph 572',
        'gph 575', 'gph 580', 'gph 595',
        'hci 422', 'hci 430', 'hci 441',
        'hci 445', 'hci 450', 'hci 454',
        'hci 460', 'hci 470', 'hci 511',
        'hci 512', 'hci 513', 'hci 514',
        'hci 515', 'hci 520', 'hci 522',
        'hci 530', 'hci 545', 'hci 553',
        'hci 580', 'hci 590', 'hci 594',
        'hci 596', 'hci 599', 'hci 690',
        'hit 421', 'hit 422', 'hit 430',
        'hit 440', 'hit 451', 'hit 511',
        'hit 515', 'is 431', 'is 433',
        'is 440', 'is 452', 'is 456',
        'is 482', 'is 486', 'is 500',
        'is 505', 'is 506', 'is 511',
        'is 549', 'is 550', 'is 570',
        'is 574', 'is 579', 'is 580',
        'is 590', 'is 596', 'is 599',
        'is 690', 'is 696', 'is 698',
        'it 432', 'it 590', 'it 599',
        'it 698', 'pm 430', 'pm 440',
        'pm 535', 'pm 556', 'pm 570',
        'pm 577', 'se 433', 'se 441',
        'se 450', 'se 452', 'se 453',
        'se 456', 'se 457', 'se 459',
        'se 468', 'se 475', 'se 477',
        'se 480', 'se 482', 'se 491',
        'se 511', 'se 525', 'se 526',
        'se 529', 'se 533', 'se 546',
        'se 549', 'se 554', 'se 556',
        'se 560', 'se 579', 'se 581',
        'se 582', 'se 591', 'se 598',
        'se 599', 'se 690', 'se 691',
        'se 695', 'se 696', 'se 698',
        'se 699', 'tdc 431', 'tdc 460',
        'tdc 463', 'tdc 464', 'tdc 468',
        'tdc 477', 'tdc 478', 'tdc 484',
        'tdc 511', 'tdc 512', 'tdc 514',
        'tdc 532', 'tdc 542', 'tdc 560',
        'tdc 562', 'tdc 563', 'tdc 567',
        'tdc 568', 'tdc 577', 'tdc 593',
        'tdc 594', 'tdc 599', 'tdc 690',
        'tdc 696', 'tdc 698']),
    'capstones': set([
        'is 577']),
    'majElects': set([
        'ect 424', 'is 444', 'ect 480',
        'is 483', 'hci 440', 'is 431',
        'is 440', 'is 455', 'is 540',
        'is 556', 'is 565', 'is 578']),
    'gradReqs': [0, 4, 2, 1, 1, 0, 5]
# Indexes correspond to the number of intro, foundation, major electives, open electives, capstones, courses \
# from a single concentration required for graduation, and advanced_courses
})


IS_DBA = Curriculum(**{
    'intros': set([
        'it 411']),
    'foundations': set([
        'is 421', 'csc 451', 'is 422',
        'is 430']),
    'advCourses': set([
        'is 549', 'csc 454', 'csc 452',
        'csc 554']),
    'openElects': set([
        'cns 450', 'cns 455', 'cns 466',
        'cns 477', 'cns 488', 'cns 489',
        'cns 490', 'cns 533', 'cns 587',
        'cns 594', 'cns 597', 'cns 599',
        'csc 421', 'csc 426', 'csc 431',
        'csc 435', 'csc 436', 'csc 438',
        'csc 439', 'csc 440', 'csc 443',
        'csc 444', 'csc 447', 'csc 448',
        'csc 453', 'csc 457', 'csc 458',
        'csc 461', 'csc 462', 'csc 471',
        'csc 472', 'csc 475', 'csc 480',
        'csc 481', 'csc 482', 'csc 485',
        'csc 486', 'csc 489', 'csc 491',
        'csc 492', 'csc 500', 'csc 503',
        'csc 521', 'csc 525', 'csc 528',
        'csc 531', 'csc 534', 'csc 535',
        'csc 536', 'csc 538', 'csc 540',
        'csc 543', 'csc 547', 'csc 548',
        'csc 549', 'csc 550', 'csc 551',
        'csc 552', 'csc 553', 'csc 555',
        'csc 557', 'csc 559', 'csc 575',
        'csc 576', 'csc 577', 'csc 578',
        'csc 580', 'csc 583', 'csc 587',
        'csc 588', 'csc 589', 'csc 590',
        'csc 591', 'csc 592', 'csc 594',
        'csc 595', 'csc 598', 'csc 599',
        'csc 601', 'csc 690', 'csc 695',
        'csc 696', 'csc 697', 'csc 698',
        'csc 699', 'ect 424', 'ect 436',
        'ect 455', 'ect 480', 'ect 481',
        'ect 556', 'ect 565', 'ect 582',
        'ect 583', 'ect 586', 'ect 587',
        'ect 589', 'ect 596', 'ect 690',
        'ect 696', 'ect 698', 'gam 424',
        'gam 425', 'gam 426', 'gam 427',
        'gam 428', 'gam 430', 'gam 440',
        'gam 450', 'gam 451', 'gam 453',
        'gam 462', 'gam 470', 'gam 475',
        'gam 476', 'gam 486', 'gam 491',
        'gam 499', 'gam 520', 'gam 530',
        'gam 540', 'gam 550', 'gam 575',
        'gam 576', 'gam 594', 'gam 597',
        'gam 598', 'gam 599', 'gam 600',
        'gam 690', 'gam 691', 'gam 695',
        'gph 425', 'gph 436', 'gph 438',
        'gph 448', 'gph 450', 'gph 469',
        'gph 487', 'gph 536', 'gph 538',
        'gph 539', 'gph 540', 'gph 541',
        'gph 560', 'gph 565', 'gph 570',
        'gph 572', 'gph 575', 'gph 580',
        'gph 595', 'hci 422', 'hci 430',
        'hci 440', 'hci 441', 'hci 445',
        'hci 450', 'hci 454', 'hci 460',
        'hci 470', 'hci 511', 'hci 512',
        'hci 513', 'hci 514', 'hci 515',
        'hci 520', 'hci 522', 'hci 530',
        'hci 545', 'hci 553', 'hci 580',
        'hci 590', 'hci 594', 'hci 596',
        'hci 599', 'hci 690', 'hit 421',
        'hit 422', 'hit 430', 'hit 440',
        'hit 451', 'hit 511', 'hit 515',
        'is 431', 'is 433', 'is 435',
        'is 440', 'is 444', 'is 455',
        'is 456', 'is 482', 'is 483',
        'is 485', 'is 486', 'is 500',
        'is 506', 'is 511', 'is 535',
        'is 540', 'is 556', 'is 560',
        'is 565', 'is 570', 'is 574',
        'is 578', 'is 579', 'is 580',
        'is 590', 'is 596', 'is 599',
        'is 690', 'is 696', 'is 698',
        'it 432', 'it 590', 'it 599',
        'it 698', 'pm 430', 'pm 440',
        'pm 535', 'pm 556', 'pm 570',
        'pm 577', 'se 430', 'se 433',
        'se 441', 'se 450', 'se 452',
        'se 453', 'se 456', 'se 457',
        'se 459', 'se 468', 'se 475',
        'se 477', 'se 480', 'se 482',
        'se 491', 'se 511', 'se 525',
        'se 526', 'se 529', 'se 533',
        'se 546', 'se 549', 'se 554',
        'se 556', 'se 560', 'se 579',
        'se 581', 'se 582', 'se 591',
        'se 598', 'se 599', 'se 690',
        'se 691', 'se 695', 'se 696',
        'se 698', 'se 699', 'tdc 431',
        'tdc 460', 'tdc 463', 'tdc 464',
        'tdc 468', 'tdc 477', 'tdc 478',
        'tdc 484', 'tdc 511', 'tdc 512',
        'tdc 514', 'tdc 532', 'tdc 542',
        'tdc 560', 'tdc 562', 'tdc 563',
        'tdc 567', 'tdc 568', 'tdc 577',
        'tdc 593', 'tdc 594', 'tdc 599',
        'tdc 690', 'tdc 696', 'tdc 698']),
    'capstones': set([
        'is 577']),
    'majElects': set([
        'cns 440', 'ipd 447', 'ipd 451',
        'ipd 460', 'ipd 463', 'is 452',
        'is 505', 'is 536', 'is 550']),
    'gradReqs': [1, 4, 3, 1, 1, 0, 4]
# Indexes correspond to the number of intro, foundation, major electives, open electives, capstones, courses \
# from a single concentration required for graduation, and advanced_courses
})


IS_BI = Curriculum(**{
    'intros': set([
        'csc 401', 'it 403']),
    'foundations': set([
        'is 421', 'csc 451', 'is 422',
        'is 430']),
    'advCourses': set([
        'is 574', 'csc 423', 'is 467',
        'is 549']),
    'openElects': set([
        'cns 440', 'cns 450', 'cns 455',
        'cns 466', 'cns 477', 'cns 488',
        'cns 489', 'cns 490', 'cns 533',
        'cns 587', 'cns 594', 'cns 597',
        'cns 599', 'csc 421', 'csc 426',
        'csc 431', 'csc 435', 'csc 436',
        'csc 438', 'csc 439', 'csc 440',
        'csc 443', 'csc 444', 'csc 447',
        'csc 448', 'csc 452',
        'csc 453', 'csc 454', 'csc 457',
        'csc 458', 'csc 461', 'csc 462',
        'csc 471', 'csc 472', 'csc 475',
        'csc 480', 'csc 481', 'csc 482',
        'csc 485', 'csc 486', 'csc 489',
        'csc 491', 'csc 492', 'csc 500',
        'csc 503', 'csc 521', 'csc 525',
        'csc 528', 'csc 531', 'csc 534',
        'csc 535', 'csc 536', 'csc 538',
        'csc 540', 'csc 543', 'csc 547',
        'csc 548', 'csc 549', 'csc 550',
        'csc 551', 'csc 552', 'csc 553',
        'csc 554', 'csc 555', 'csc 557',
        'csc 559', 'csc 576',
        'csc 577', 'csc 578', 'csc 580',
        'csc 583', 'csc 587', 'csc 588',
        'csc 589', 'csc 590', 'csc 591',
        'csc 592', 'csc 594', 'csc 595',
        'csc 598', 'csc 599', 'csc 601',
        'csc 690', 'csc 695', 'csc 696',
        'csc 697', 'csc 698', 'csc 699',
        'ect 424', 'ect 436', 'ect 455',
        'ect 480', 'ect 481', 'ect 556',
        'ect 565', 'ect 582', 'ect 583',
        'ect 586', 'ect 587', 'ect 589',
        'ect 596', 'ect 690', 'ect 696',
        'ect 698', 'gam 424', 'gam 425',
        'gam 426', 'gam 427', 'gam 428',
        'gam 430', 'gam 440', 'gam 450',
        'gam 451', 'gam 453', 'gam 462',
        'gam 470', 'gam 475', 'gam 476',
        'gam 486', 'gam 491', 'gam 499',
        'gam 520', 'gam 530', 'gam 540',
        'gam 550', 'gam 575', 'gam 576',
        'gam 594', 'gam 597', 'gam 598',
        'gam 599', 'gam 600', 'gam 690',
        'gam 691', 'gam 695', 'gph 425',
        'gph 436', 'gph 438', 'gph 448',
        'gph 450', 'gph 469', 'gph 487',
        'gph 536', 'gph 538', 'gph 539',
        'gph 540', 'gph 541', 'gph 560',
        'gph 565', 'gph 570', 'gph 572',
        'gph 575', 'gph 580', 'gph 595',
        'hci 422', 'hci 430', 'hci 440',
        'hci 441', 'hci 445', 'hci 450',
        'hci 454', 'hci 460', 'hci 470',
        'hci 511', 'hci 513',
        'hci 514', 'hci 515', 'hci 520',
        'hci 522', 'hci 530', 'hci 545',
        'hci 553', 'hci 580', 'hci 590',
        'hci 594', 'hci 596', 'hci 599',
        'hci 690', 'hit 421', 'hit 422',
        'hit 430', 'hit 440', 'hit 451',
        'hit 511', 'hit 515', 'is 431',
        'is 433', 'is 435', 'is 440',
        'is 444', 'is 455',
        'is 482', 'is 483',
        'is 485', 'is 486', 'is 500',
        'is 505', 'is 506', 'is 511',
        'is 535', 'is 540',
        'is 556', 'is 560',
        'is 565', 'is 570',
        'is 577', 'is 578', 'is 579',
        'is 580', 'is 590', 'is 596',
        'is 599', 'is 690', 'is 696',
        'is 698', 'it 432', 'it 590',
        'it 599', 'it 698', 'pm 430',
        'pm 440', 'pm 535', 'pm 556',
        'pm 570', 'pm 577', 'se 430',
        'se 433', 'se 441', 'se 450',
        'se 452', 'se 453', 'se 456',
        'se 457', 'se 459', 'se 468',
        'se 475', 'se 477', 'se 480',
        'se 482', 'se 491', 'se 511',
        'se 525', 'se 526', 'se 529',
        'se 533', 'se 546', 'se 549',
        'se 554', 'se 556', 'se 560',
        'se 579', 'se 581', 'se 582',
        'se 591', 'se 598', 'se 599',
        'se 690', 'se 691', 'se 695',
        'se 696', 'se 698', 'se 699',
        'tdc 431', 'tdc 460', 'tdc 463',
        'tdc 464', 'tdc 468', 'tdc 477',
        'tdc 478', 'tdc 484', 'tdc 511',
        'tdc 512', 'tdc 514', 'tdc 532',
        'tdc 542', 'tdc 560', 'tdc 562',
        'tdc 563', 'tdc 567', 'tdc 568',
        'tdc 577', 'tdc 593', 'tdc 594',
        'tdc 599', 'tdc 690', 'tdc 696',
        'tdc 698']),
    'capstones': set([
        'is 577']),
    'majElects': set([
        'csc 424', 'csc 465', 'csc 495',
        'csc 575', 'ect 584', 'geo 441',
        'hci 512', 'ipd 447', 'ipd 451',
        'ipd 460', 'is 452', 'is 456',
        'is 536', 'is 550']),
    'gradReqs': [2, 4, 3, 1, 1, 0, 4]
# Indexes correspond to the number of intro, foundation, major electives, open electives, capstones, courses \
# from a single concentration required for graduation, and advanced_courses
})

IS_IT = Curriculum(**{
    'foundations': set([
        'is 421', 'csc 451', 'is 422',
        'is 430']),
    'advCourses': set([
        'ect 424', 'is 556', 'is 570',
        'is 535']),
    'openElects': set([
        'cns 450', 'cns 455', 'cns 466',
        'cns 477', 'cns 488', 'cns 489',
        'cns 490', 'cns 533', 'cns 587',
        'cns 594', 'cns 597', 'cns 599',
        'csc 421', 'csc 426', 'csc 431',
        'csc 435', 'csc 436', 'csc 438',
        'csc 439', 'csc 440', 'csc 443',
        'csc 444', 'csc 447', 'csc 448',
        'csc 452', 'csc 453', 'csc 454',
        'csc 457', 'csc 458', 'csc 461',
        'csc 462', 'csc 471', 'csc 472',
        'csc 475', 'csc 480', 'csc 481',
        'csc 482', 'csc 485', 'csc 486',
        'csc 489', 'csc 491', 'csc 492',
        'csc 500', 'csc 503', 'csc 521',
        'csc 525', 'csc 528', 'csc 531',
        'csc 534', 'csc 535', 'csc 536',
        'csc 538', 'csc 540', 'csc 543',
        'csc 547', 'csc 548', 'csc 549',
        'csc 550', 'csc 551', 'csc 552',
        'csc 553', 'csc 554', 'csc 555',
        'csc 557', 'csc 559', 'csc 575',
        'csc 576', 'csc 577', 'csc 578',
        'csc 580', 'csc 583', 'csc 587',
        'csc 588', 'csc 589', 'csc 590',
        'csc 591', 'csc 592', 'csc 594',
        'csc 595', 'csc 598', 'csc 599',
        'csc 601', 'csc 690', 'csc 695',
        'csc 696', 'csc 697', 'csc 698',
        'csc 699', 'ect 436', 'ect 455',
        'ect 480', 'ect 481', 'ect 565',
        'ect 582', 'ect 583', 'ect 586',
        'ect 587', 'ect 589', 'ect 596',
        'ect 690', 'ect 696', 'ect 698',
        'gam 424', 'gam 425', 'gam 426',
        'gam 427', 'gam 428', 'gam 430',
        'gam 440', 'gam 450', 'gam 451',
        'gam 453', 'gam 462', 'gam 470',
        'gam 475', 'gam 476', 'gam 486',
        'gam 491', 'gam 499', 'gam 520',
        'gam 530', 'gam 540', 'gam 550',
        'gam 575', 'gam 576', 'gam 594',
        'gam 597', 'gam 598', 'gam 599',
        'gam 600', 'gam 690', 'gam 691',
        'gam 695', 'gph 425', 'gph 436',
        'gph 438', 'gph 448', 'gph 450',
        'gph 469', 'gph 487', 'gph 536',
        'gph 538', 'gph 539', 'gph 540',
        'gph 541', 'gph 560', 'gph 565',
        'gph 570', 'gph 572', 'gph 575',
        'gph 580', 'gph 595', 'hci 422',
        'hci 430', 'hci 440', 'hci 441',
        'hci 445', 'hci 450', 'hci 454',
        'hci 460', 'hci 470', 'hci 511',
        'hci 512', 'hci 513', 'hci 514',
        'hci 515', 'hci 520', 'hci 522',
        'hci 530', 'hci 545', 'hci 553',
        'hci 580', 'hci 590', 'hci 594',
        'hci 596', 'hci 599', 'hci 690',
        'hit 421', 'hit 422', 'hit 430',
        'hit 440', 'hit 451', 'hit 511',
        'hit 515', 'is 431', 'is 433',
        'is 452', 'is 455', 'is 485',
        'is 486', 'is 511', 'is 549',
        'is 574', 'is 578', 'is 590',
        'is 596', 'is 599', 'is 690',
        'is 696', 'is 698', 'it 432',
        'it 590', 'it 599', 'it 698',
        'pm 430', 'pm 440', 'pm 535',
        'pm 556', 'pm 570', 'pm 577',
        'se 430', 'se 433', 'se 441',
        'se 450', 'se 452', 'se 453',
        'se 456', 'se 457', 'se 459',
        'se 468', 'se 475', 'se 477',
        'se 480', 'se 482', 'se 491',
        'se 511', 'se 525', 'se 526',
        'se 529', 'se 533', 'se 546',
        'se 549', 'se 554', 'se 556',
        'se 560', 'se 579', 'se 581',
        'se 582', 'se 591', 'se 598',
        'se 599', 'se 690', 'se 691',
        'se 695', 'se 696', 'se 698',
        'se 699', 'tdc 431', 'tdc 460',
        'tdc 463', 'tdc 464', 'tdc 468',
        'tdc 477', 'tdc 478', 'tdc 484',
        'tdc 511', 'tdc 512', 'tdc 514',
        'tdc 532', 'tdc 542', 'tdc 560',
        'tdc 562', 'tdc 563', 'tdc 567',
        'tdc 568', 'tdc 577', 'tdc 593',
        'tdc 594', 'tdc 599', 'tdc 690',
        'tdc 696', 'tdc 698']),
    'capstones': set([
        'is 577']),
    'majElects': set([
        'cns 440', 'ect 556', 'is 440',
        'is 444', 'is 482', 'is 483',
        'is 500', 'is 505', 'is 506',
        'is 535', 'is 536', 'is 540',
        'is 550', 'is 560', 'is 565',
        'is 579', 'is 580']),
    'gradReqs': [0, 4, 3, 1, 1, 0, 4]
# Indexes correspond to the number of intro, foundation, major electives, open electives, capstones, courses \
# from a single concentration required for graduation, and advanced_courses
})
