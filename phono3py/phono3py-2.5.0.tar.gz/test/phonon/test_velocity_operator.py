"""Tests for velocity operator calculation."""
import numpy as np
from phonopy import Phonopy
from phonopy.units import THzToCm, VaspToTHz

from phono3py.phonon.velocity_operator import VelocityOperator


def test_gv_operator_nacl(ph_nacl: Phonopy):
    """Test of VelocityOperator for NaCl."""
    gv_operator_square_modulus_ref = {}
    # direction 0
    gv_operator_square_modulus_ref[0] = np.array(
        [
            [
                2.376573179312185289e02 + 0.000000000000000000e00j,
                4.617045673846550957e-02 + 0.000000000000000000e00j,
                1.659427710087436544e-03 + 0.000000000000000000e00j,
                1.845589427959312538e-04 + 0.000000000000000000e00j,
                5.246392004787010954e00 + 0.000000000000000000e00j,
                3.417043258882670759e-04 + 0.000000000000000000e00j,
            ],
            [
                4.617045673846550957e-02 + 0.000000000000000000e00j,
                2.058631263030552248e02 + 0.000000000000000000e00j,
                6.691174335294252273e01 + 0.000000000000000000e00j,
                2.134043678391127907e-01 + 0.000000000000000000e00j,
                5.212855408005317645e-03 + 0.000000000000000000e00j,
                2.354617277954078047e-01 + 0.000000000000000000e00j,
            ],
            [
                1.659427710087436544e-03 + 0.000000000000000000e00j,
                6.691174335294252273e01 + 0.000000000000000000e00j,
                9.658082636210202736e02 + 0.000000000000000000e00j,
                8.616265783185071969e-01 + 0.000000000000000000e00j,
                4.452485294432699634e-04 + 0.000000000000000000e00j,
                1.328146717651219610e00 + 0.000000000000000000e00j,
            ],
            [
                1.845589427959312538e-04 + 0.000000000000000000e00j,
                2.134043678391127907e-01 + 0.000000000000000000e00j,
                8.616265783185071969e-01 + 0.000000000000000000e00j,
                1.623813633632023301e-01 + 0.000000000000000000e00j,
                3.493899327316501123e-03 + 0.000000000000000000e00j,
                4.031373352398433252e-02 + 0.000000000000000000e00j,
            ],
            [
                5.246392004787010954e00 + 0.000000000000000000e00j,
                5.212855408005317645e-03 + 0.000000000000000000e00j,
                4.452485294432699634e-04 + 0.000000000000000000e00j,
                3.493899327316501123e-03 + 0.000000000000000000e00j,
                5.509054909199991634e00 + 0.000000000000000000e00j,
                1.634636477879549202e-02 + 0.000000000000000000e00j,
            ],
            [
                3.417043258882670759e-04 + 0.000000000000000000e00j,
                2.354617277954078047e-01 + 0.000000000000000000e00j,
                1.328146717651219610e00 + 0.000000000000000000e00j,
                4.031373352398433252e-02 + 0.000000000000000000e00j,
                1.634636477879549202e-02 + 0.000000000000000000e00j,
                5.330574757358162969e02 - 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    gv_operator_square_modulus_ref[1] = np.array(
        [
            [
                1.884774558511167868e02 + 0.000000000000000000e00j,
                1.797869399641995880e-01 + 0.000000000000000000e00j,
                3.238489047675335297e-01 + 0.000000000000000000e00j,
                3.098759078351569565e-02 + 0.000000000000000000e00j,
                1.246504907432090636e00 + 0.000000000000000000e00j,
                1.700549291066742047e-02 + 0.000000000000000000e00j,
            ],
            [
                1.797869399641995880e-01 + 0.000000000000000000e00j,
                5.282405827344455247e02 + 0.000000000000000000e00j,
                2.054235131085235651e02 + 0.000000000000000000e00j,
                1.509896397430046555e01 + 0.000000000000000000e00j,
                1.654722059026667372e-02 + 0.000000000000000000e00j,
                4.980129780913235216e00 + 0.000000000000000000e00j,
            ],
            [
                3.238489047675335297e-01 + 0.000000000000000000e00j,
                2.054235131085235651e02 + 0.000000000000000000e00j,
                6.589198152555901800e01 + 0.000000000000000000e00j,
                1.129132939208696174e00 + 0.000000000000000000e00j,
                3.285051725497791929e-04 + 0.000000000000000000e00j,
                1.010437576958299388e01 + 0.000000000000000000e00j,
            ],
            [
                3.098759078351569565e-02 + 0.000000000000000000e00j,
                1.509896397430046555e01 + 0.000000000000000000e00j,
                1.129132939208696174e00 + 0.000000000000000000e00j,
                2.412737678456116726e02 - 0.000000000000000000e00j,
                6.231727918633763602e-02 + 0.000000000000000000e00j,
                3.706451256602802573e02 + 0.000000000000000000e00j,
            ],
            [
                1.246504907432090636e00 + 0.000000000000000000e00j,
                1.654722059026667372e-02 + 0.000000000000000000e00j,
                3.285051725497791929e-04 + 0.000000000000000000e00j,
                6.231727918633763602e-02 + 0.000000000000000000e00j,
                2.923045062435118080e00 + 0.000000000000000000e00j,
                2.546207887156830552e-01 + 0.000000000000000000e00j,
            ],
            [
                1.700549291066742047e-02 + 0.000000000000000000e00j,
                4.980129780913235216e00 + 0.000000000000000000e00j,
                1.010437576958299388e01 + 0.000000000000000000e00j,
                3.706451256602802573e02 + 0.000000000000000000e00j,
                2.546207887156830552e-01 + 0.000000000000000000e00j,
                7.731035849319536801e00 + 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    gv_operator_square_modulus_ref[2] = np.array(
        [
            [
                1.881052607505289131e-01 - 0.000000000000000000e00j,
                5.178350546270510080e01 + 0.000000000000000000e00j,
                2.534873723262373630e02 + 0.000000000000000000e00j,
                2.207833653630836279e-02 + 0.000000000000000000e00j,
                1.527349290129506945e-02 + 0.000000000000000000e00j,
                1.639778012628040571e01 + 0.000000000000000000e00j,
            ],
            [
                5.178350546270510080e01 + 0.000000000000000000e00j,
                1.389419421313752290e00 - 0.000000000000000000e00j,
                1.003906059730161671e00 + 0.000000000000000000e00j,
                2.081704192112629871e-04 + 0.000000000000000000e00j,
                1.229252569768010561e00 + 0.000000000000000000e00j,
                5.095701459942430372e-02 + 0.000000000000000000e00j,
            ],
            [
                2.534873723262373630e02 + 0.000000000000000000e00j,
                1.003906059730161671e00 + 0.000000000000000000e00j,
                3.486606694013737462e-01 - 0.000000000000000000e00j,
                6.138672393593642886e-04 + 0.000000000000000000e00j,
                2.502226006188104090e-01 + 0.000000000000000000e00j,
                5.535791067786596797e-02 + 0.000000000000000000e00j,
            ],
            [
                2.207833653630836279e-02 + 0.000000000000000000e00j,
                2.081704192112629871e-04 + 0.000000000000000000e00j,
                6.138672393593642886e-04 + 0.000000000000000000e00j,
                5.799711445058541165e-03 + 0.000000000000000000e00j,
                1.586504048028407610e01 + 0.000000000000000000e00j,
                2.669183331996494712e-01 + 0.000000000000000000e00j,
            ],
            [
                1.527349290129506945e-02 + 0.000000000000000000e00j,
                1.229252569768010561e00 + 0.000000000000000000e00j,
                2.502226006188104090e-01 + 0.000000000000000000e00j,
                1.586504048028407610e01 + 0.000000000000000000e00j,
                1.384495835228062299e00 + 0.000000000000000000e00j,
                8.415872471952644673e02 + 0.000000000000000000e00j,
            ],
            [
                1.639778012628040571e01 + 0.000000000000000000e00j,
                5.095701459942430372e-02 + 0.000000000000000000e00j,
                5.535791067786596797e-02 + 0.000000000000000000e00j,
                2.669183331996494712e-01 + 0.000000000000000000e00j,
                8.415872471952644673e02 + 0.000000000000000000e00j,
                4.059989780585400165e-01 - 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    eigvals_NaCl_Ref = np.array(
        [
            7.609317325541059773e00,
            9.775005093981388171e00,
            2.762788346050308874e01,
            3.914697185310215133e01,
            4.805770120097133713e01,
            8.718205400809350181e01,
        ]
    )

    gv_operator = VelocityOperator(
        ph_nacl.dynamical_matrix, symmetry=ph_nacl.primitive_symmetry
    )

    # we chose an 'ugly' q-point because we want to avoid degeneracies.
    ph_nacl.dynamical_matrix.run([[0.1, 0.22, 0.33]])
    dm = ph_nacl.dynamical_matrix.dynamical_matrix
    eigvals, eigvecs = np.linalg.eigh(dm)

    np.testing.assert_allclose(
        eigvals * VaspToTHz * THzToCm,
        eigvals_NaCl_Ref,
        atol=0.00001,
        rtol=0.00001,
    )

    # we chose an 'ugly' q-point because we want to avoid degeneracies.
    # degeneracies are tested in phono3py
    gv_operator.run([[0.1, 0.22, 0.33]])
    square_modulus_q = np.zeros((6, 6, 3), dtype=np.complex128)
    for direction in range(0, 3):
        vel_op = gv_operator.velocity_operators[0][:, :, direction]
        for id_i in range(0, 6):
            for id_j in range(0, 6):
                square_modulus_q[id_i, id_j, direction] = (
                    vel_op[id_i, id_j] * vel_op[id_j, id_i]
                )

        np.testing.assert_allclose(
            (square_modulus_q[:, :, direction]).ravel(),
            gv_operator_square_modulus_ref[direction].ravel(),
            atol=1e-3,
        )


def test_gv_operator_si(ph_si: Phonopy):
    """Test of VelocityOperator for Si."""
    gv_operator_square_modulus_ref = {}
    # direction 0
    gv_operator_square_modulus_ref[0] = np.array(
        [
            [
                8.703598564667423716e02 + 0.000000000000000000e00j,
                3.852114314423075170e-01 + 0.000000000000000000e00j,
                5.164775587373296730e02 + 0.000000000000000000e00j,
                1.824424707490242548e-01 + 0.000000000000000000e00j,
                1.349080727393703910e03 + 0.000000000000000000e00j,
                3.960327334115312098e-02 + 0.000000000000000000e00j,
            ],
            [
                3.852114314423075170e-01 + 0.000000000000000000e00j,
                9.111110193530701054e02 + 0.000000000000000000e00j,
                2.266175142048653779e00 + 0.000000000000000000e00j,
                1.167386014484261977e03 + 0.000000000000000000e00j,
                3.901569003294572013e00 + 0.000000000000000000e00j,
                6.355778683852354334e02 + 0.000000000000000000e00j,
            ],
            [
                5.164775587373296730e02 + 0.000000000000000000e00j,
                2.266175142048653779e00 + 0.000000000000000000e00j,
                3.328578674715060515e03 + 0.000000000000000000e00j,
                2.330816831647273268e00 + 0.000000000000000000e00j,
                3.088688700184525260e02 + 0.000000000000000000e00j,
                1.447794488148178127e00 + 0.000000000000000000e00j,
            ],
            [
                1.824424707490242548e-01 + 0.000000000000000000e00j,
                1.167386014484261977e03 + 0.000000000000000000e00j,
                2.330816831647273268e00 + 0.000000000000000000e00j,
                2.888366773060061519e02 - 0.000000000000000000e00j,
                7.059885784894146324e-03 + 0.000000000000000000e00j,
                4.859250138694907739e-01 + 0.000000000000000000e00j,
            ],
            [
                1.349080727393703910e03 + 0.000000000000000000e00j,
                3.901569003294572013e00 + 0.000000000000000000e00j,
                3.088688700184525260e02 + 0.000000000000000000e00j,
                7.059885784894146324e-03 + 0.000000000000000000e00j,
                1.243378632569180553e02 - 0.000000000000000000e00j,
                3.318710696308258771e-03 + 0.000000000000000000e00j,
            ],
            [
                3.960327334115312098e-02 + 0.000000000000000000e00j,
                6.355778683852354334e02 + 0.000000000000000000e00j,
                1.447794488148178127e00 + 0.000000000000000000e00j,
                4.859250138694907739e-01 + 0.000000000000000000e00j,
                3.318710696308258771e-03 + 0.000000000000000000e00j,
                8.803667409305997182e01 - 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    # direction 1
    gv_operator_square_modulus_ref[1] = np.array(
        [
            [
                3.005739528154802720e00 + 0.000000000000000000e00j,
                1.090506497460818736e00 + 0.000000000000000000e00j,
                1.781783016342926203e03 + 0.000000000000000000e00j,
                9.898148052483902726e-01 + 0.000000000000000000e00j,
                1.714671696405686987e02 + 0.000000000000000000e00j,
                1.097330242598429373e-02 + 0.000000000000000000e00j,
            ],
            [
                1.090506497460818736e00 + 0.000000000000000000e00j,
                1.197463525274162521e03 + 0.000000000000000000e00j,
                2.174162640813394720e00 + 0.000000000000000000e00j,
                2.780305393861517018e02 + 0.000000000000000000e00j,
                2.243456039259525969e00 + 0.000000000000000000e00j,
                7.246604124718528510e02 + 0.000000000000000000e00j,
            ],
            [
                1.781783016342926203e03 + 0.000000000000000000e00j,
                2.174162640813394720e00 + 0.000000000000000000e00j,
                5.217090573193127057e02 + 0.000000000000000000e00j,
                1.442659458687336471e00 + 0.000000000000000000e00j,
                6.629770305067837626e02 + 0.000000000000000000e00j,
                6.410569298900631319e-02 + 0.000000000000000000e00j,
            ],
            [
                9.898148052483902726e-01 + 0.000000000000000000e00j,
                2.780305393861517018e02 + 0.000000000000000000e00j,
                1.442659458687336471e00 + 0.000000000000000000e00j,
                1.331644422043883935e02 - 0.000000000000000000e00j,
                3.887979991194636525e-02 + 0.000000000000000000e00j,
                1.074310057118949580e01 + 0.000000000000000000e00j,
            ],
            [
                1.714671696405686987e02 + 0.000000000000000000e00j,
                2.243456039259525969e00 + 0.000000000000000000e00j,
                6.629770305067837626e02 + 0.000000000000000000e00j,
                3.887979991194636525e-02 + 0.000000000000000000e00j,
                2.577509129395529897e00 - 0.000000000000000000e00j,
                1.901409113872518444e-02 + 0.000000000000000000e00j,
            ],
            [
                1.097330242598429373e-02 + 0.000000000000000000e00j,
                7.246604124718528510e02 + 0.000000000000000000e00j,
                6.410569298900631319e-02 + 0.000000000000000000e00j,
                1.074310057118949580e01 + 0.000000000000000000e00j,
                1.901409113872518444e-02 + 0.000000000000000000e00j,
                9.539659480379510725e00 - 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    gv_operator_square_modulus_ref[2] = np.array(
        [
            [
                5.243734036781237950e-01 - 0.000000000000000000e00j,
                1.157407659025238615e02 + 0.000000000000000000e00j,
                3.511112818202297148e-01 + 0.000000000000000000e00j,
                3.027286387385743072e-01 + 0.000000000000000000e00j,
                1.204586331136705324e00 + 0.000000000000000000e00j,
                1.420789242486925559e03 + 0.000000000000000000e00j,
            ],
            [
                1.157407659025238615e02 + 0.000000000000000000e00j,
                9.714049991295321540e-01 + 0.000000000000000000e00j,
                2.445426867563387532e03 + 0.000000000000000000e00j,
                5.387895796274706495e-01 + 0.000000000000000000e00j,
                1.204290668993368030e01 + 0.000000000000000000e00j,
                1.699364828801638971e00 + 0.000000000000000000e00j,
            ],
            [
                3.511112818202297148e-01 + 0.000000000000000000e00j,
                2.445426867563387532e03 + 0.000000000000000000e00j,
                4.772359176983208329e00 - 0.000000000000000000e00j,
                3.956853010905875863e02 + 0.000000000000000000e00j,
                1.626635436775644372e00 + 0.000000000000000000e00j,
                8.291129162568002187e01 + 0.000000000000000000e00j,
            ],
            [
                3.027286387385743072e-01 + 0.000000000000000000e00j,
                5.387895796274706495e-01 + 0.000000000000000000e00j,
                3.956853010905875863e02 + 0.000000000000000000e00j,
                3.855094469950215430e-01 + 0.000000000000000000e00j,
                2.205792575908791875e01 + 0.000000000000000000e00j,
                1.741493768927920502e-02 + 0.000000000000000000e00j,
            ],
            [
                1.204586331136705324e00 + 0.000000000000000000e00j,
                1.204290668993368030e01 + 0.000000000000000000e00j,
                1.626635436775644372e00 + 0.000000000000000000e00j,
                2.205792575908791875e01 + 0.000000000000000000e00j,
                6.163891418145815183e-04 + 0.000000000000000000e00j,
                6.746537532808173587e00 + 0.000000000000000000e00j,
            ],
            [
                1.420789242486925559e03 + 0.000000000000000000e00j,
                1.699364828801638971e00 + 0.000000000000000000e00j,
                8.291129162568002187e01 + 0.000000000000000000e00j,
                1.741493768927920502e-02 + 0.000000000000000000e00j,
                6.746537532808173587e00 + 0.000000000000000000e00j,
                8.511045046101584424e-03 + 0.000000000000000000e00j,
            ],
        ],
        dtype=np.complex128,
    )

    eigvals_si_Ref = np.array(
        [
            1.517927660706452642e01,
            2.515082879969709140e01,
            9.696599540972319176e01,
            4.355143205292288826e02,
            4.476500173090510657e02,
            4.587899457528906169e02,
        ]
    )

    gv_operator = VelocityOperator(
        ph_si.dynamical_matrix, symmetry=ph_si.primitive_symmetry
    )

    ph_si.dynamical_matrix.run([[0.1, 0.22, 0.33]])
    dm = ph_si.dynamical_matrix.dynamical_matrix
    eigvals, eigvecs = np.linalg.eigh(dm)

    np.testing.assert_allclose(
        eigvals * VaspToTHz * THzToCm,
        eigvals_si_Ref,
        atol=0.00001,
        rtol=0.00001,
    )

    gv_operator.run([[0.1, 0.22, 0.33]])
    square_modulus_q = np.zeros((6, 6, 3), dtype=np.complex128)
    for direction in range(0, 3):
        vel_op = gv_operator.velocity_operators[0][:, :, direction]
        for id_i in range(0, 6):
            for id_j in range(0, 6):
                square_modulus_q[id_i, id_j, direction] = (
                    vel_op[id_i, id_j] * vel_op[id_j, id_i]
                )
        np.testing.assert_allclose(
            square_modulus_q[:, :, direction].ravel(),
            gv_operator_square_modulus_ref[direction].ravel(),
            atol=1e-5,
        )
