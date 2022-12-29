from cga_py import conditions as con
from cga_py import cga_object as cg
from cga_py import GeometryError
import numpy as np
import numpy.testing as nt


def test_study_cond():
    a = cg(
        np.array(
            [
                844.94424921,
                200.2260122,
                565.29703616,
                517.1192215,
                548.71211879,
                -982.0077644,
                434.89547631,
                930.81244647,
                721.32643468,
                -683.79338806,
                256.38840576,
                -355.69394934,
                681.53327362,
                -22.67814807,
                -107.08448605,
                -40.46962442,
                -996.95261258,
                830.73946602,
                777.66477061,
                716.48772892,
                959.13937444,
                -904.77431682,
                68.89817051,
                745.33768046,
                -109.06817517,
                -966.88535839,
                -488.53225325,
                602.89326163,
                375.97793653,
                -250.05151507,
                828.61258309,
                737.38156624,
            ]
        )
    )
    # b = cg(
    # np.array(
    # [
    # 725.11011632,
    # -975.08265755,
    # 144.70651935,
    # 38.38948582,
    # -471.52565452,
    # -635.02557765,
    # 830.61336759,
    # 224.20132730,
    # 707.70612438,
    # 899.80033113,
    # 68.54020623,
    # 408.10948996,
    # 960.27688338,
    # 88.25762321,
    # 726.74012486,
    # 55.61095813,
    # -652.38752758,
    # 545.21429166,
    # -966.77157658,
    # -899.58613452,
    # 559.06038443,
    # -587.10321068,
    # -298.20056367,
    # -758.32329002,
    # 446.03370508,
    # -616.11082366,
    # 342.97958509,
    # 337.41571782,
    # 416.78904346,
    # 498.01600767,
    # 139.74679988,
    # 755.44123826,
    # ]
    # )
    # )
    x = cg(np.arange(32) + 1)
    # c = np.array(
    # [
    # 4.436332211 * 10**6,
    # -2.392569265 * 10**6,
    # 990351.779,
    # 3.900844337 * 10**6,
    # -8.520393554 * 10**6,
    # -3.122850310 * 10**6,
    # -1.701858230 * 10**6,
    # 275489.8173,
    # 0.001,
    # -0.001,
    # 3.707288811 * 10**6,
    # -0.003,
    # -0.0020,
    # -0.001,
    # 0.001,
    # 0.0034,
    # 6.022785987 * 10**6,
    # -0.0002,
    # 0,
    # -0.0026,
    # 0.0001,
    # -0.0011,
    # 0.002,
    # -0.002,
    # -0.001,
    # -0.0033,
    # -2.040725498 * 10**6,
    # 8.870422856 * 10**6,
    # -1.701858235 * 10**6,
    # 275489.8186,
    # 3.707288808 * 10**6,
    # 6.022785985 * 10**6,
    # ]
    # )
    d = np.array(
        [
            -327021.5061,
            -278920.5336,
            50152.37721,
            13527.37001,
            -220728.6829,
            119350.8810,
            90579.46766,
            -130583.3196,
            0,
            -0.00012,
            -20805.23254,
            -0.0001,
            -0.00005,
            0.00001,
            -0.00001,
            -0.00014,
            -61936.77022,
            0,
            0.00003,
            -0.0000211,
            -0.00003,
            -0.00004,
            0.00005,
            0,
            -0.00012,
            -0.00019,
            49523.88473,
            27677.89392,
            90579.46773,
            -130583.3198,
            -20805.23270,
            -61936.76996,
        ]
    )
    x1 = np.array(
        [
            -247227.7505,
            -232978.6964,
            -9432.58039,
            68223.17069,
            -110364.3415,
            59675.44049,
            30540.57647,
            -82177.74483,
            151174.5294,
            -43383.69247,
            -10179.22422,
            101925.9636,
            65808.33910,
            -21745.44597,
            -48872.65159,
            -83716.99754,
            -43887.60621,
            122119.2781,
            47416.42211,
            817.4768789,
            -46124.09375,
            -93518.42964,
            -16682.45868,
            -18296.90926,
            -34508.76899,
            61459.48564,
            24761.94235,
            13838.94696,
            45289.73387,
            -65291.65985,
            -10402.61631,
            -30968.38482,
        ]
    )
    x2 = np.array(
        [
            -79793.75560,
            -45941.83722,
            59584.95760,
            -54695.80068,
            -110364.3414,
            59675.44051,
            60038.89119,
            -48405.57474,
            -151174.5294,
            43383.69235,
            -10626.00832,
            -101925.9637,
            -65808.33915,
            21745.44598,
            48872.65158,
            83716.99740,
            -18049.16401,
            -122119.2781,
            -47416.42208,
            -817.47690,
            46124.09372,
            93518.42960,
            16682.45873,
            18296.90926,
            34508.76887,
            -61459.48583,
            24761.94238,
            13838.94696,
            45289.73386,
            -65291.65991,
            -10402.61639,
            -30968.38514,
        ]
    )

    print((con.study_cond(a, x)).coeff - d)
    nt.assert_allclose((a * (~x)).coeff, x1)
    nt.assert_allclose((x * (~a)).coeff, x2)
    # nt.assert_allclose((a * (~x) + x * (~a)).coeff, d)
    # nt.assert_allclose(con.study_cond(a, x).coeff, d)
    # nt.assert_allclose(con.study_cond(a, b).coeff, c)


def test_study_var():
    a = cg(
        np.array(
            [
                844.94424921,
                200.2260122,
                565.29703616,
                517.1192215,
                548.71211879,
                -982.0077644,
                434.89547631,
                930.81244647,
                721.32643468,
                -683.79338806,
                256.38840576,
                -355.69394934,
                681.53327362,
                -22.67814807,
                -107.08448605,
                -40.46962442,
                -996.95261258,
                830.73946602,
                777.66477061,
                716.48772892,
                959.13937444,
                -904.77431682,
                68.89817051,
                745.33768046,
                -109.06817517,
                -966.88535839,
                -488.53225325,
                602.89326163,
                375.97793653,
                -250.05151507,
                828.61258309,
                737.38156624,
            ]
        )
    )
    b = cg(
        np.array(
            [
                725.11011632,
                -975.08265755,
                144.70651935,
                38.38948582,
                -471.52565452,
                -635.02557765,
                830.61336759,
                224.20132730,
                707.70612438,
                899.80033113,
                68.54020623,
                408.10948996,
                960.27688338,
                88.25762321,
                726.74012486,
                55.61095813,
                -652.38752758,
                545.21429166,
                -966.77157658,
                -899.58613452,
                559.06038443,
                -587.10321068,
                -298.20056367,
                -758.32329002,
                446.03370508,
                -616.11082366,
                342.97958509,
                337.41571782,
                416.78904346,
                498.01600767,
                139.74679988,
                755.44123826,
            ]
        )
    )
    c = np.array(
        [
            -918943.9838,
            1.365678104 * 10**6,
            583667.2476,
            -266359.9978,
            764052.5956,
            357883.4934,
            382468.9808,
            -769406.4871,
            480461.1493,
            412043.9181,
        ]
    )
    d = np.array(
        [
            218382.3708,
            -205353.6606,
            568403.5239,
            783552.5933,
            309358.0182,
            -250392.1223,
            -104144.0574,
            222280.2191,
            -86634.00579,
            68355.7328,
        ]
    )

    nt.assert_allclose(con.study_var(a), c)
    nt.assert_allclose(con.study_var(b), d)


def test_null_quad_err():
    with nt.assert_raises(GeometryError):
        con.null_quadric(cg(np.arange(32)))


def test_null_quad():
    a = cg(np.random.rand(16), True)
    assert con.null_quadric(a) == (a * (~a)).coeff[0]
