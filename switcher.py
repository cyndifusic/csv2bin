# Change this to select a target .bin file.

selectFile = 0

# File indices:
#
# 0 - Find Mii 1P (wanted_1p_leveltable.bin)
# 1 - Table Tennis (leveltable.bin)
# 2 - Table Tennis (rallyleveluptable.bin)
# 3 - Shooting Range (DucBalloonParam.bin)
# 4 - Shooting Range (DucCircleMatoParam.bin)
# 5 - Shooting Range (DucClayParam.bin)

templates = [

                # 0

                [
                    ["wly_1p_leveltable", ["", 
                                           "miiNum", 
                                           "behavior", 
                                           "goal", 
                                           "field", 
                                           "zoomMin", 
                                           "zoomMax", 
                                           "baseZ", 
                                           "width",
                                           "height", 
                                           "darkZ", 
                                           "hoverScale", 
                                           "spotLightScaleX", 
                                           "spotLightScaleY", 
                                           "spotLightScaleZ", 
                                           "spotLightOffsetX", 
                                           "spotLightOffsetY"], "wanted_1p_leveltable", [4, "I", 12, "f"], 1, 99]
                ],

                # 1
                
                [
                    ["pnp_leveltable", ["", 
                                        "easyChance", 
                                        "mediumChance", 
                                        "hardChance"], "leveltable", [3, "I"], 0, 13]
                ],

                # 2

                [
                    ["pnp_rallyleveluptable", ["rally", 
                                               "level", 
                                               "power"], "rallyleveluptable", [2, "I", 1, "f"], -1, 217]
                ],

                # 3

                [
                    ["duc_balloons", ["",
                                      "velocityDecay",
                                      "value",
                                      "baseSize",
                                      "?",
                                      "?",
                                      "stringCullLen",
                                      "?",
                                      "stringOffset",
                                      "tiltSpeed",
                                      "tiltAngle"], "DucBalloonParam", [1, "f", 1, "I", 6, "f", 1, "I", 1, "f"], -1, 1],

                    ["duc_balloons", ["",
                                      "hitboxSize",
                                      "velocityY",
                                      "velocityX",
                                      "modelSize"], "DucBalloonParam", [4, "f"], 1, 8],

                    ["duc_balloons", ["",
                                      "segment1Len",
                                      "segment2Len",
                                      "segment3Len",
                                      "segment4Len",
                                      "?"], "DucBalloonParam", [5, "f"], -1, 1]
                ],

                # 4

                [
                    ["duc_targets", ["",
                                     "?",
                                     "?",
                                     "?",
                                     "?",
                                     "?",
                                     "bonusValue1",
                                     "bonusValue2",
                                     "regularValue1",
                                     "regularValue2",
                                     "faceGoodValue1",
                                     "faceGoodValue2",
                                     "faceBadValue1",
                                     "faceBadValue2",
                                     "baseSize",
                                     "posXScaleWide",
                                     "posYScaleWide",
                                     "posZWide",
                                     "posXBaseWide",
                                     "posYBaseWide",
                                     "posXScaleStd",
                                     "posYScaleStd",
                                     "posZStd",
                                     "posXBaseStd",
                                     "posYBaseStd"], "DucCircleMatoParam", [5, "f", 6, "I", 2, "i", 11, "f"], -1, 1],

                    ["duc_targets", ["",
                                     "hitboxSizeWide",
                                     "hitboxSizeStd",
                                     "modelSizeWide",
                                     "modelSizeStd",
                                     "spinTime",
                                     "waitTime1",
                                     "waitTime2"], "DucCircleMatoParam", [4, "f", 3, "I"], 1, 8]
                ],

                # 5

                [
                    ["duc_frisbees", ["",
                                      "velocityDecay",
                                      "maxSpinZ",
                                      "spinUpZ",
                                      "earlyZ",
                                      "earlyValue",
                                      "lateValue",
                                      "baseSize",
                                      "rotateDecay",
                                      "rotateVelocity"], "DucClayParam", [4, "f", 2, "I", 3, "f"], -1, 1],

                    ["duc_frisbees", ["",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "?",
                                      "maxDropVel",
                                      "dropAccel",
                                      "modelSize",
                                      "velocity"], "DucClayParam", [14, "f"], 1, 8]
                ],

            ]

tmpl = templates[selectFile]
