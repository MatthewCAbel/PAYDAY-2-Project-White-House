Hooks:PostHook(BlackMarketTweakData, "_init_weapon_skins", "AKMagpulAssistMagsModInit", function(self)
	self.weapon_skins.akmsu_lones.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("mtr_magpul"):key()] = {
			base_gradient = Idstring("units/payday2_cash/safes/sfs/base_gradient/base_sfs_010_df"),
			uv_offset_rot = Vector3(0.397329, 1.01141, 4.72475),
			uv_scale = Vector3(4.69642, 1.02547, 1),
			sticker = Idstring("units/payday2_cash/safes/lones/sticker/lones_sticker_014_df")
		},
		[Idstring("akm_mag"):key()] = {
			uv_offset_rot = Vector3(0.149297, 0.616743, 0.648849),
			uv_scale = Vector3(8.22435, 8.03365, 1)
		}
	}
	self.weapon_skins.x_akmsu_wac.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("mtr_magpul"):key()] = {
			base_gradient = Idstring("units/payday2_cash/safes/wac/base_gradient/base_wac_012_df")
		},
		[Idstring("akm_mag"):key()] = {
			uv_scale = Vector3(1, 1, 0)
		}
	}
	self.weapon_skins.akm_mxs.parts.wpn_fps_upg_ak_m_quick = nil
	self.weapon_skins.flint_cs4.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("mtr_magpul"):key()] = {
			pattern = "units/payday2_cash/safes/cs4/pattern/cs4_pattern_012_e_df",
			pattern_gradient = "units/payday2_cash/safes/cs4/pattern_gradient/gradient_cs4_012_d_df"
		},
		[Idstring("mat_mag"):key()] = {
			pattern = "units/payday2_cash/safes/cs4/pattern/cs4_pattern_012_b_df",
			pattern_gradient = "units/payday2_cash/safes/cs4/pattern_gradient/gradient_cs4_012_d_df",
			base_gradient = "units/payday2_cash/safes/cs4/base_gradient/base_cs4_012_c_df"
		}
	}
	self.weapon_skins.akmsu_grunt.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("akm_mag"):key()] = {
			base_gradient = Idstring("units/payday2_cash/safes/bah/base_gradient/base_bah_003_b_df"),
			uv_offset_rot = Vector3(0.0484394, 0.832616, 0.169331),
			uv_scale = Vector3(5.64992, 5.60224, 1),
			sticker = Idstring("units/payday2_cash/safes/grunt/sticker/grunt_sticker_009_df")
		}
	}
	self.weapon_skins.akm_tam.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("akm_mag"):key()] = {
			pattern_tweak = Vector3(1.20678, 0, 1)
		}
	}
-- flint_css = AK17 RIFLE | EVA
	self.weapon_skins.flint_css.parts.wpn_fps_upg_ak_m_quick = {
		[Idstring("mat_mag"):key()] = {
			pattern = "units/payday2_cash/safes/css/pattern/css_pattern_010_b_df",
			pattern_gradient = "units/payday2_cash/safes/css/pattern_gradient/gradient_css_010_df",
			base_gradient = Idstring("units/payday2_cash/safes/css/base_gradient/base_css_010_b_df")
		},
		[Idstring("mtr_magpul"):key()] = {
			base_gradient = "units/payday2_cash/safes/css/base_gradient/base_css_010_df"
		}
	}
-- akm_nin = AK.762 RIFLE | Magma Knight
	self.weapon_skins.akm_nin.parts.wpn_fps_upg_ak_m_quick = {
		b2ed2a5a86e2a95b = {
			base_gradient = Idstring("units/payday2_cash/safes/nin/base_gradient/nin_base_gradient_009_01_df"),
			pattern_pos = Vector3(-0.0560371, 0.0448997, 0),
			pattern = Idstring("units/payday2_cash/safes/nin/pattern/nin_pattern_009_02_df"),
			pattern_tweak = Vector3(1.097, 0, 1)
		},
		["47fd1974bc0ea7b7"] = {
			base_gradient = Idstring("units/payday2_cash/safes/nin/base_gradient/nin_base_gradient_009_02_df")
		}
	}
end)