"""Tests for grids."""
from __future__ import annotations

import numpy as np
import pytest
from phonopy import Phonopy
from phonopy.structure.atoms import PhonopyAtoms
from phonopy.structure.symmetry import Symmetry

from phono3py import Phono3py
from phono3py.other.tetrahedron_method import get_tetrahedra_relative_grid_address
from phono3py.phonon.grid import (
    BZGrid,
    _get_grid_points_by_bz_rotations_c,
    _get_grid_points_by_bz_rotations_py,
    _get_grid_points_by_rotations,
    can_use_std_lattice,
    get_grid_point_from_address,
    get_grid_point_from_address_py,
    get_ir_grid_points,
)


def _get_qpoints(adrs, bzgrid):
    return np.dot(
        (adrs * 2 + bzgrid.PS) / bzgrid.D_diag.astype("double") / 2, bzgrid.Q.T
    )


def test_get_grid_point_from_address(agno2_cell):
    """Test for get_grid_point_from_address.

    Compare get_grid_point_from_address from spglib and that
    written in python with mesh numbers.

    """
    mesh = (10, 10, 10)

    for address in list(np.ndindex(mesh)):
        gp_spglib = get_grid_point_from_address(address, mesh)
        gp_py = get_grid_point_from_address_py(address, mesh)
        # print("%s %d %d" % (address, gp_spglib, gp_py))
        np.testing.assert_equal(gp_spglib, gp_py)


def test_BZGrid(si_pbesol_111: Phono3py):
    """Tests of BZGrid type1 and type2."""
    lat = si_pbesol_111.primitive.cell
    reclat = np.linalg.inv(lat)
    mesh = [4, 4, 4]

    gp_map2 = [
        0,
        1,
        2,
        4,
        5,
        6,
        7,
        8,
        9,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        34,
        35,
        36,
        40,
        41,
        43,
        44,
        46,
        47,
        48,
        49,
        50,
        54,
        56,
        57,
        59,
        60,
        61,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        77,
        78,
        79,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
    ]

    bzgrid1 = BZGrid(mesh, lattice=lat, store_dense_gp_map=False)
    bzgrid2 = BZGrid(mesh, lattice=lat, store_dense_gp_map=True)

    adrs1 = bzgrid1.addresses[: np.prod(mesh)]
    adrs2 = bzgrid2.addresses[bzgrid2.gp_map[:-1]]
    assert ((adrs1 - adrs2) % mesh == 0).all()
    np.testing.assert_equal(bzgrid1.addresses.shape, bzgrid2.addresses.shape)
    # print("".join(["%d, " % i for i in bzgrid2.gp_map.ravel()]))
    np.testing.assert_equal(bzgrid2.gp_map.ravel(), gp_map2)

    dist1 = np.sqrt((np.dot(adrs1, reclat.T) ** 2).sum(axis=1))
    dist2 = np.sqrt((np.dot(adrs2, reclat.T) ** 2).sum(axis=1))
    np.testing.assert_allclose(dist1, dist2, atol=1e-8)


def test_BZGrid_bzg2grg(si_pbesol_111):
    """Test of mapping of BZGrid to GRGrid.

    This mapping table is stored in BZGrid, but also determined by
    get_grid_point_from_address. This test checks the consistency.

    """
    lat = si_pbesol_111.primitive.cell
    mesh = [4, 4, 4]
    bzgrid1 = BZGrid(mesh, lattice=lat, store_dense_gp_map=False)
    grg = []
    for i in range(len(bzgrid1.addresses)):
        grg.append(get_grid_point_from_address(bzgrid1.addresses[i], mesh))
    np.testing.assert_equal(grg, bzgrid1.bzg2grg)

    bzgrid2 = BZGrid(mesh, lattice=lat, store_dense_gp_map=True)
    grg = []
    for i in range(len(bzgrid2.addresses)):
        grg.append(get_grid_point_from_address(bzgrid2.addresses[i], mesh))
    np.testing.assert_equal(grg, bzgrid2.bzg2grg)


def test_BZGrid_SNF(si_pbesol_111: Phono3py):
    """Test of SNF in BZGrid."""
    lat = si_pbesol_111.primitive.cell
    mesh = 10
    bzgrid1 = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=si_pbesol_111.primitive_symmetry.dataset,
        use_grg=True,
        store_dense_gp_map=False,
    )
    _test_BZGrid_SNF(bzgrid1)

    bzgrid2 = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=si_pbesol_111.primitive_symmetry.dataset,
        use_grg=True,
        store_dense_gp_map=True,
    )
    _test_BZGrid_SNF(bzgrid2)


def test_BZGrid_SNF_with_tmat(si_pbesol_111: Phono3py):
    """Test of SNF in BZGrid with transformation matrix."""
    lat = si_pbesol_111.primitive.cell
    mesh = 10
    tmat = [[0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0]]
    bzgrid1 = BZGrid(
        mesh,
        lattice=lat,
        transformation_matrix=tmat,
        use_grg=True,
    )
    _test_BZGrid_SNF(bzgrid1)


def test_BZGrid_SNF_with_no_tmat_and_dataset(si_pbesol_111: Phono3py):
    """Test of SNF in BZGrid with transformation matrix."""
    lat = si_pbesol_111.primitive.cell
    mesh = 10
    with pytest.raises(RuntimeError):
        BZGrid(
            mesh,
            lattice=lat,
            use_grg=True,
        )


def test_BZGrid_SNF_with_negative_tmat(si_pbesol_111: Phono3py):
    """Test of SNF in BZGrid with negative transformation matrix."""
    lat = si_pbesol_111.primitive.cell
    mesh = 10
    tmat = [[0.0, -0.5, -0.5], [-0.5, 0.0, -0.5], [-0.5, -0.5, 0.0]]
    with pytest.raises(RuntimeError):
        BZGrid(
            mesh,
            lattice=lat,
            transformation_matrix=tmat,
            use_grg=True,
        )


def test_BZGrid_SNF_with_non_integer_inv_tmat(si_pbesol_111: Phono3py):
    """Test of SNF in BZGrid with negative transformation matrix."""
    lat = si_pbesol_111.primitive.cell
    mesh = 10
    tmat = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    with pytest.raises(RuntimeError):
        BZGrid(
            mesh,
            lattice=lat,
            transformation_matrix=tmat,
            use_grg=True,
        )


def _test_BZGrid_SNF(bzgrid: BZGrid):
    # from phonopy.structure.atoms import PhonopyAtoms
    # from phonopy.interface.vasp import get_vasp_structure_lines

    A = bzgrid.grid_matrix
    D_diag = bzgrid.D_diag
    P = bzgrid.P
    Q = bzgrid.Q
    np.testing.assert_equal(np.dot(P, np.dot(A, Q)), np.diag(D_diag))

    # print(D_diag)
    # grg2bzg = bzgrid.grg2bzg
    # qpoints = np.dot(bzgrid.addresses[grg2bzg], bzgrid.QDinv.T)
    # cell = PhonopyAtoms(cell=np.linalg.inv(lat).T,
    #                     scaled_positions=qpoints,
    #                     numbers=[1,] * len(qpoints))
    # print("\n".join(get_vasp_structure_lines(cell)))

    gr_addresses = bzgrid.addresses[bzgrid.grg2bzg]
    # print(D_diag)
    # print(len(gr_addresses))
    # for line in gr_addresses.reshape(-1, 12):
    #     print("".join(["%d, " % i for i in line]))

    ref = [
        0,
        0,
        0,
        -1,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        -2,
        0,
        -1,
        -2,
        0,
        0,
        -1,
        0,
        -1,
        -1,
        0,
        0,
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        2,
        1,
        1,
        2,
        1,
        0,
        -1,
        1,
        -1,
        -1,
        1,
        0,
        0,
        -2,
        -1,
        0,
        -2,
        0,
        1,
        2,
        1,
        1,
        2,
        0,
        -2,
        -2,
        -1,
        -2,
        -2,
        0,
        -1,
        -2,
        -1,
        -1,
        -2,
        0,
        0,
        -1,
        -1,
        0,
        -1,
        0,
        1,
        -1,
        -1,
        1,
        -1,
        0,
        -2,
        -1,
        -1,
        -2,
        -1,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
    ]

    assert (
        ((np.reshape(ref, (-1, 3)) - gr_addresses) % bzgrid.D_diag).ravel() == 0
    ).all()

    if bzgrid.symmetry_dataset is not None:
        ref_rots = [
            1,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            0,
            0,
            2,
            1,
            -1,
            2,
            2,
            -1,
            1,
            0,
            0,
            2,
            -1,
            0,
            4,
            0,
            -1,
            1,
            0,
            0,
            0,
            -1,
            1,
            2,
            -2,
            1,
            -1,
            0,
            0,
            0,
            -1,
            0,
            -2,
            -2,
            1,
            -1,
            0,
            0,
            0,
            1,
            -1,
            0,
            0,
            -1,
            -1,
            0,
            0,
            -2,
            1,
            0,
            -2,
            2,
            -1,
            -1,
            0,
            0,
            -2,
            -1,
            1,
            -4,
            0,
            1,
            -1,
            -1,
            1,
            0,
            -1,
            1,
            -2,
            -1,
            2,
            -1,
            -1,
            1,
            0,
            -2,
            1,
            0,
            -3,
            2,
            -1,
            -1,
            1,
            -2,
            -1,
            1,
            -2,
            -3,
            2,
            -1,
            -1,
            1,
            -2,
            0,
            1,
            -4,
            -1,
            2,
            1,
            1,
            -1,
            0,
            1,
            -1,
            0,
            3,
            -2,
            1,
            1,
            -1,
            2,
            0,
            -1,
            2,
            1,
            -2,
            1,
            1,
            -1,
            2,
            1,
            -1,
            4,
            1,
            -2,
            1,
            1,
            -1,
            0,
            2,
            -1,
            2,
            3,
            -2,
            -1,
            1,
            0,
            -2,
            0,
            1,
            -2,
            1,
            1,
            -1,
            1,
            0,
            -2,
            1,
            0,
            -4,
            1,
            1,
            -1,
            1,
            0,
            0,
            2,
            -1,
            -2,
            3,
            -1,
            -1,
            1,
            0,
            0,
            1,
            0,
            0,
            3,
            -1,
            1,
            -1,
            0,
            2,
            0,
            -1,
            4,
            -1,
            -1,
            1,
            -1,
            0,
            0,
            -1,
            0,
            2,
            -1,
            -1,
            1,
            -1,
            0,
            0,
            -2,
            1,
            0,
            -3,
            1,
            1,
            -1,
            0,
            2,
            -1,
            0,
            2,
            -3,
            1,
            -1,
            0,
            0,
            0,
            -1,
            0,
            0,
            0,
            -1,
            -1,
            0,
            0,
            -2,
            -1,
            1,
            -2,
            -2,
            1,
            -1,
            0,
            0,
            -2,
            1,
            0,
            -4,
            0,
            1,
            -1,
            0,
            0,
            0,
            1,
            -1,
            -2,
            2,
            -1,
            1,
            0,
            0,
            0,
            1,
            0,
            2,
            2,
            -1,
            1,
            0,
            0,
            0,
            -1,
            1,
            0,
            0,
            1,
            1,
            0,
            0,
            2,
            -1,
            0,
            2,
            -2,
            1,
            1,
            0,
            0,
            2,
            1,
            -1,
            4,
            0,
            -1,
            1,
            1,
            -1,
            0,
            1,
            -1,
            2,
            1,
            -2,
            1,
            1,
            -1,
            0,
            2,
            -1,
            0,
            3,
            -2,
            1,
            1,
            -1,
            2,
            1,
            -1,
            2,
            3,
            -2,
            1,
            1,
            -1,
            2,
            0,
            -1,
            4,
            1,
            -2,
            -1,
            -1,
            1,
            0,
            -1,
            1,
            0,
            -3,
            2,
            -1,
            -1,
            1,
            -2,
            0,
            1,
            -2,
            -1,
            2,
            -1,
            -1,
            1,
            -2,
            -1,
            1,
            -4,
            -1,
            2,
            -1,
            -1,
            1,
            0,
            -2,
            1,
            -2,
            -3,
            2,
            1,
            -1,
            0,
            2,
            0,
            -1,
            2,
            -1,
            -1,
            1,
            -1,
            0,
            2,
            -1,
            0,
            4,
            -1,
            -1,
            1,
            -1,
            0,
            0,
            -2,
            1,
            2,
            -3,
            1,
            1,
            -1,
            0,
            0,
            -1,
            0,
            0,
            -3,
            1,
            -1,
            1,
            0,
            -2,
            0,
            1,
            -4,
            1,
            1,
            -1,
            1,
            0,
            0,
            1,
            0,
            -2,
            1,
            1,
            -1,
            1,
            0,
            0,
            2,
            -1,
            0,
            3,
            -1,
            -1,
            1,
            0,
            -2,
            1,
            0,
            -2,
            3,
            -1,
        ]

        np.testing.assert_equal(ref_rots, bzgrid.rotations.ravel())


def test_BZGrid_SNF_hexagonal(aln_lda):
    """Test of SNF in BZGrid."""
    lat = aln_lda.primitive.cell
    mesh = 20
    bzgrid = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=aln_lda.primitive_symmetry.dataset,
    )
    np.testing.assert_equal(bzgrid.D_diag, [7, 7, 4])

    bzgrid = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=aln_lda.primitive_symmetry.dataset,
        use_grg=True,
    )
    np.testing.assert_equal(bzgrid.D_diag, [7, 7, 4])

    bzgrid = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=aln_lda.primitive_symmetry.dataset,
        use_grg=True,
        force_SNF=True,
    )
    np.testing.assert_equal(bzgrid.D_diag, [1, 7, 28])

    bzgrid = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=aln_lda.primitive_symmetry.dataset,
        use_grg=True,
        force_SNF=True,
        SNF_coordinates="direct",
    )
    np.testing.assert_equal(bzgrid.D_diag, [1, 6, 30])


def test_BZGrid_SNF_nonprimitive(si_pbesol_111):
    """Test of SNF in BZGrid."""
    lat = si_pbesol_111.supercell.cell
    mesh = 20
    with pytest.warns(
        RuntimeWarning, match="Non primitive cell input. Unable to use GR-grid."
    ):
        bzgrid = BZGrid(
            mesh,
            lattice=lat,
            symmetry_dataset=si_pbesol_111.symmetry.dataset,
            use_grg=True,
        )
    np.testing.assert_equal(bzgrid.D_diag, [4, 4, 4])
    identity = np.eye(3, dtype=int)
    np.testing.assert_equal(bzgrid.P, identity)
    np.testing.assert_equal(bzgrid.Q, identity)


def test_SNF_tetrahedra_relative_grid(aln_lda):
    """Test relative grid addresses under GR-grid.

    Under GR-grid, grid point addressing becomes different from ordinal uniform
    grid. But P and Q matrices can be used to map betweewn these grid systems.
    In this test, the agreement is checked by representing them in Cartesian
    coordinates.

    """
    lat = aln_lda.primitive.cell
    mesh = 25

    for snf_coordinates, d_diag in zip(
        ("direct", "reciprocal"), ([2, 8, 24], [1, 9, 45])
    ):
        bzgrid = BZGrid(
            mesh,
            lattice=lat,
            symmetry_dataset=aln_lda.primitive_symmetry.dataset,
            use_grg=True,
            force_SNF=True,
            SNF_coordinates=snf_coordinates,
        )

        np.testing.assert_equal(bzgrid.D_diag, d_diag)

        plat = np.linalg.inv(aln_lda.primitive.cell)
        mlat = bzgrid.microzone_lattice
        tetrahedra = get_tetrahedra_relative_grid_address(mlat)
        snf_tetrahedra = np.dot(tetrahedra, bzgrid.P.T)

        for mtet, ptet in zip(tetrahedra, snf_tetrahedra):
            np.testing.assert_allclose(
                np.dot(mtet, mlat.T),
                np.dot(np.dot(ptet, bzgrid.QDinv.T), plat.T),
                atol=1e-8,
            )


def test_get_grid_points_by_bz_rotations(si_pbesol_111):
    """Rotate grid point by rotations with and without considering BZ surface.

    The following three methods are tested between type-1 and type-2.

        _get_grid_points_by_rotations
        _get_grid_points_by_bz_rotations_c
        _get_grid_points_by_bz_rotations_py

    """
    ref10_type1 = [
        10,
        26,
        10,
        26,
        26,
        10,
        26,
        10,
        88,
        80,
        200,
        208,
        200,
        208,
        88,
        80,
        208,
        88,
        80,
        200,
        208,
        88,
        80,
        200,
        26,
        10,
        26,
        10,
        10,
        26,
        10,
        26,
        200,
        208,
        88,
        80,
        88,
        80,
        200,
        208,
        80,
        200,
        208,
        88,
        80,
        200,
        208,
        88,
    ]
    ref12_type2 = [
        12,
        39,
        12,
        39,
        39,
        12,
        39,
        12,
        122,
        109,
        265,
        278,
        265,
        278,
        122,
        109,
        278,
        122,
        109,
        265,
        278,
        122,
        109,
        265,
        39,
        12,
        39,
        12,
        12,
        39,
        12,
        39,
        265,
        278,
        122,
        109,
        122,
        109,
        265,
        278,
        109,
        265,
        278,
        122,
        109,
        265,
        278,
        122,
    ]

    ref10_bz_type1 = [
        10,
        26,
        260,
        270,
        269,
        258,
        271,
        259,
        88,
        285,
        200,
        328,
        322,
        208,
        291,
        286,
        327,
        292,
        287,
        321,
        326,
        290,
        80,
        323,
        269,
        258,
        271,
        259,
        10,
        26,
        260,
        270,
        200,
        328,
        88,
        285,
        291,
        286,
        322,
        208,
        80,
        323,
        326,
        290,
        287,
        321,
        327,
        292,
    ]
    ref12_bz_type2 = [
        12,
        39,
        15,
        41,
        40,
        13,
        42,
        14,
        122,
        110,
        265,
        281,
        267,
        278,
        124,
        111,
        280,
        125,
        112,
        266,
        279,
        123,
        109,
        268,
        40,
        13,
        42,
        14,
        12,
        39,
        15,
        41,
        265,
        281,
        122,
        110,
        124,
        111,
        267,
        278,
        109,
        268,
        279,
        123,
        112,
        266,
        280,
        125,
    ]

    lat = si_pbesol_111.primitive.cell
    mesh = 20

    bz_grid_type1 = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=si_pbesol_111.primitive_symmetry.dataset,
        use_grg=True,
        store_dense_gp_map=False,
    )
    bz_grid_type2 = BZGrid(
        mesh,
        lattice=lat,
        symmetry_dataset=si_pbesol_111.primitive_symmetry.dataset,
        use_grg=True,
        store_dense_gp_map=True,
    )

    # Check data consistency by reducing to GR-grid.
    # Grid point 10 in type-1 and 12 in type-2 are the same points in GR-grid.
    assert bz_grid_type1.bzg2grg[10] == bz_grid_type2.bzg2grg[12]
    np.testing.assert_equal(
        bz_grid_type1.bzg2grg[ref10_type1], bz_grid_type2.bzg2grg[ref12_type2]
    )
    np.testing.assert_equal(
        bz_grid_type1.bzg2grg[ref10_type1], bz_grid_type1.bzg2grg[ref10_bz_type1]
    )
    np.testing.assert_equal(
        bz_grid_type1.bzg2grg[ref10_type1], bz_grid_type2.bzg2grg[ref12_bz_type2]
    )

    bzgps = _get_grid_points_by_rotations(10, bz_grid_type1, bz_grid_type1.rotations)
    np.testing.assert_equal(bzgps, ref10_type1)

    bzgps = _get_grid_points_by_rotations(12, bz_grid_type2, bz_grid_type2.rotations)
    np.testing.assert_equal(bzgps, ref12_type2)

    bzgps = _get_grid_points_by_bz_rotations_c(
        10, bz_grid_type1, bz_grid_type1.rotations
    )
    np.testing.assert_equal(bzgps, ref10_bz_type1)

    bzgps = _get_grid_points_by_bz_rotations_c(
        12, bz_grid_type2, bz_grid_type2.rotations
    )
    np.testing.assert_equal(bzgps, ref12_bz_type2)

    bzgps = _get_grid_points_by_bz_rotations_py(
        10, bz_grid_type1, bz_grid_type1.rotations
    )
    np.testing.assert_equal(bzgps, ref10_bz_type1)

    bzgps = _get_grid_points_by_bz_rotations_py(
        12, bz_grid_type2, bz_grid_type2.rotations
    )
    np.testing.assert_equal(bzgps, ref12_bz_type2)

    # Exhaustive consistency check among methods
    for grgp in range(np.prod(bz_grid_type1.D_diag)):
        bzgp_type1 = bz_grid_type1.grg2bzg[grgp]
        bzgp_type2 = bz_grid_type2.grg2bzg[grgp]

        rot_grgps = bz_grid_type1.bzg2grg[
            _get_grid_points_by_rotations(
                bzgp_type1, bz_grid_type1, bz_grid_type1.rotations
            )
        ]

        np.testing.assert_equal(
            rot_grgps,
            bz_grid_type2.bzg2grg[
                _get_grid_points_by_rotations(
                    bzgp_type2, bz_grid_type2, bz_grid_type2.rotations
                )
            ],
        )

        np.testing.assert_equal(
            _get_grid_points_by_bz_rotations_c(
                bzgp_type1, bz_grid_type1, bz_grid_type1.rotations
            ),
            _get_grid_points_by_bz_rotations_py(
                bzgp_type1, bz_grid_type1, bz_grid_type1.rotations
            ),
        )

        np.testing.assert_equal(
            _get_grid_points_by_bz_rotations_c(
                bzgp_type2, bz_grid_type2, bz_grid_type2.rotations
            ),
            _get_grid_points_by_bz_rotations_py(
                bzgp_type2, bz_grid_type2, bz_grid_type2.rotations
            ),
        )

        np.testing.assert_equal(
            rot_grgps,
            bz_grid_type1.bzg2grg[
                _get_grid_points_by_bz_rotations_c(
                    bzgp_type1, bz_grid_type1, bz_grid_type1.rotations
                )
            ],
        )

        np.testing.assert_equal(
            rot_grgps,
            bz_grid_type2.bzg2grg[
                _get_grid_points_by_bz_rotations_c(
                    bzgp_type2, bz_grid_type2, bz_grid_type2.rotations
                )
            ],
        )

    # for gps in bzgps.reshape(-1, 12):
    #     print("".join(["%d, " % gp for gp in gps]))


def test_can_use_std_lattice():
    """Test of can_use_std_lattice."""
    conv_lat = [[6.06531185, 0.0, 0.0], [0.0, 0.0, 6.06531185], [0.0, -6.06531185, 0.0]]
    std_lattice = [
        [6.06531185, 0.0, 0.0],
        [0.0, 6.06531185, 0.0],
        [0.0, 0.0, 6.06531185],
    ]
    tmat = [[0.0, 0.5, 0.5], [-0.5, -0.5, 0.0], [0.5, 0.0, 0.5]]
    rotations = [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[0, 1, 0], [0, 0, 1], [-1, -1, -1]],
        [[0, 0, 1], [-1, -1, -1], [1, 0, 0]],
        [[-1, -1, -1], [1, 0, 0], [0, 1, 0]],
        [[-1, -1, -1], [0, 0, 1], [0, 1, 0]],
        [[1, 0, 0], [-1, -1, -1], [0, 0, 1]],
        [[0, 1, 0], [1, 0, 0], [-1, -1, -1]],
        [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
        [[-1, -1, -1], [1, 0, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 1, 0], [-1, -1, -1]],
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [-1, -1, -1], [0, 1, 0]],
        [[1, 0, 0], [-1, -1, -1], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
        [[0, 0, 1], [0, 1, 0], [-1, -1, -1]],
        [[-1, -1, -1], [0, 0, 1], [1, 0, 0]],
        [[0, 1, 0], [-1, -1, -1], [0, 0, 1]],
        [[0, 0, 1], [1, 0, 0], [-1, -1, -1]],
        [[-1, -1, -1], [0, 1, 0], [1, 0, 0]],
        [[1, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
        [[-1, -1, -1], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 0, 1], [-1, -1, -1]],
        [[0, 1, 0], [-1, -1, -1], [1, 0, 0]],
    ]

    assert can_use_std_lattice(conv_lat, tmat, std_lattice, rotations)


def test_aln_BZGrid_with_shift(aln_cell: PhonopyAtoms):
    """Test BZGrid with shift using AlN."""
    mesh = [5, 5, 4]
    symmetry = Symmetry(aln_cell)

    # Without shift
    bzgrid = BZGrid(mesh, lattice=aln_cell.cell, symmetry_dataset=symmetry.dataset)
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)
    np.testing.assert_equal(
        ir_grid_points, [0, 1, 2, 6, 7, 25, 26, 27, 31, 32, 50, 51, 52, 56, 57]
    )
    np.testing.assert_equal(
        ir_grid_weights, [1, 6, 6, 6, 6, 2, 12, 12, 12, 12, 1, 6, 6, 6, 6]
    )

    # With shift
    bzgrid = BZGrid(
        mesh,
        lattice=aln_cell.cell,
        symmetry_dataset=symmetry.dataset,
        is_shift=[False, False, True],
    )
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)
    np.testing.assert_equal(ir_grid_points, [0, 1, 2, 6, 7, 25, 26, 27, 31, 32])
    np.testing.assert_equal(ir_grid_weights, [2, 12, 12, 12, 12, 2, 12, 12, 12, 12])

    q_from_phonopy = [
        [0.0000000, 0.0000000, 0.1250000],
        [0.2000000, 0.0000000, 0.1250000],
        [0.4000000, 0.0000000, 0.1250000],
        [0.2000000, 0.2000000, 0.1250000],
        [-0.6000000, 0.2000000, 0.1250000],
        [0.0000000, 0.0000000, 0.3750000],
        [0.2000000, 0.0000000, 0.3750000],
        [0.4000000, 0.0000000, 0.3750000],
        [0.2000000, 0.2000000, 0.3750000],
        [-0.6000000, 0.2000000, 0.3750000],
    ]

    for adrs, q_phonopy in zip(
        bzgrid.addresses[bzgrid.grg2bzg[ir_grid_points]], q_from_phonopy
    ):
        q = np.dot(
            bzgrid.Q, (adrs * 2 + bzgrid.PS) / bzgrid.D_diag.astype("double") / 2
        )
        diff = q - q_phonopy
        diff -= np.rint(diff)
        np.testing.assert_allclose(diff, [0, 0, 0])
        q_phonopy_norm = np.linalg.norm(np.dot(np.linalg.inv(aln_cell.cell), q_phonopy))
        q_norm = np.linalg.norm(np.dot(np.linalg.inv(aln_cell.cell), q))
        np.testing.assert_almost_equal(q_phonopy_norm, q_norm)


@pytest.mark.parametrize(
    "is_shift",
    [
        [True, False, False],
        [False, True, False],
        [True, True, False],
        [True, False, True],
        [False, True, True],
        [True, True, True],
    ],
)
def test_aln_BZGrid_with_shift_broken_symmetry(aln_cell: PhonopyAtoms, is_shift: list):
    """Test broken symmetry of BZGrid with shift using AlN."""
    mesh = [5, 5, 4]
    symmetry = Symmetry(aln_cell)

    with pytest.raises(RuntimeError):
        BZGrid(
            mesh,
            lattice=aln_cell.cell,
            symmetry_dataset=symmetry.dataset,
            is_shift=is_shift,
        )


def test_agno2_BZGrid_with_shift(agno2_cell: PhonopyAtoms):
    """Test BZGrid with shift using AgNO2."""
    mesh = 15
    ph = Phonopy(agno2_cell, supercell_matrix=[1, 1, 1], primitive_matrix="auto")

    # from phonopy.interface.vasp import get_vasp_structure_lines
    # print("\n".join(get_vasp_structure_lines(ph.primitive)))

    # Without shift
    bzgrid = BZGrid(
        mesh,
        lattice=ph.primitive.cell,
        symmetry_dataset=ph.primitive_symmetry.dataset,
        use_grg=True,
    )
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)
    np.testing.assert_equal(bzgrid.grid_matrix, [[0, 5, 5], [2, 0, 2], [3, 3, 0]])
    np.testing.assert_equal(
        ir_grid_points, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 24, 30]
    )
    np.testing.assert_equal(
        ir_grid_weights, [1, 8, 4, 4, 4, 4, 2, 8, 4, 4, 2, 2, 4, 2, 2, 2, 2, 1]
    )
    bzgrid_no_shift = bzgrid

    # Digonal elements represent orthorhombic microzone.
    shift_ref = np.diagonal(bzgrid.microzone_lattice) / 2

    # With shift +c
    bzgrid = BZGrid(
        mesh,
        lattice=ph.primitive.cell,
        symmetry_dataset=ph.primitive_symmetry.dataset,
        use_grg=True,
        is_shift=[False, False, True],
    )
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)

    np.testing.assert_equal(
        ir_grid_points, [0, 1, 2, 3, 4, 5, 11, 12, 14, 15, 17, 18, 20, 24, 30]
    )
    np.testing.assert_equal(
        ir_grid_weights, [2, 8, 4, 8, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 2]
    )

    q_shift_c = _get_qpoints(bzgrid.addresses[bzgrid.grg2bzg], bzgrid)
    q_noshift = _get_qpoints(
        bzgrid_no_shift.addresses[bzgrid_no_shift.grg2bzg], bzgrid_no_shift
    )
    diff = q_shift_c - q_noshift
    diff -= np.rint(diff)
    diff_cart = np.dot(diff, np.linalg.inv(ph.primitive.cell).T)
    np.testing.assert_allclose(diff_cart - [0, 0, 3.33538325e-02], 0, atol=1e-8)
    np.testing.assert_allclose(diff_cart[0][2], shift_ref[2], atol=1e-8)

    # With shift +a, +b
    bzgrid = BZGrid(
        mesh,
        lattice=ph.primitive.cell,
        symmetry_dataset=ph.primitive_symmetry.dataset,
        use_grg=True,
        is_shift=[True, True, False],
    )
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)

    np.testing.assert_equal(ir_grid_points, [0, 1, 2, 3, 4, 5, 6, 8, 9, 12])
    np.testing.assert_equal(ir_grid_weights, [4, 8, 8, 4, 8, 8, 4, 8, 4, 4])

    q_shift_ab = _get_qpoints(bzgrid.addresses[bzgrid.grg2bzg], bzgrid)
    diff = q_shift_ab - q_noshift
    diff -= np.rint(diff)
    diff_cart = np.dot(diff, np.linalg.inv(ph.primitive.cell).T)
    np.testing.assert_allclose(
        diff_cart - [3.03777935e-02, 3.89622460e-02, 0], 0, atol=1e-8
    )
    np.testing.assert_allclose(diff_cart[0][[0, 1]], shift_ref[[0, 1]], atol=1e-8)

    # With shift +a, +b, +c
    bzgrid = BZGrid(
        mesh,
        lattice=ph.primitive.cell,
        symmetry_dataset=ph.primitive_symmetry.dataset,
        use_grg=True,
        is_shift=[True, True, True],
    )
    ir_grid_points, ir_grid_weights, _ = get_ir_grid_points(bzgrid)

    np.testing.assert_equal(ir_grid_points, [0, 1, 2, 3, 5, 7, 8, 9])
    np.testing.assert_equal(ir_grid_weights, [8, 8, 4, 8, 8, 8, 8, 8])

    q_shift_ab = _get_qpoints(bzgrid.addresses[bzgrid.grg2bzg], bzgrid)
    diff = q_shift_ab - q_noshift
    diff -= np.rint(diff)
    diff_cart = np.dot(diff, np.linalg.inv(ph.primitive.cell).T)
    np.testing.assert_allclose(
        diff_cart - [0.03037779, 0.03896225, 0.03335383], 0, atol=1e-8
    )
    np.testing.assert_allclose(diff_cart[0], shift_ref, atol=1e-8)
