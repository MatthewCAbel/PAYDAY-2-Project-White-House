Hooks:PostHook(WeaponFactoryTweakData, "init", "AKMagpulAssistMagsModInit", function(self)
-- AKM
if not self.wpn_fps_ass_akm.override then
	self.wpn_fps_ass_akm.override = {}
end
if not self.wpn_fps_ass_akm.override.wpn_fps_upg_ak_m_quick then
	self.wpn_fps_ass_akm.override.wpn_fps_upg_ak_m_quick = {}
end
	self.wpn_fps_ass_akm.override.wpn_fps_upg_ak_m_quick.unit = "units/mods/weapons/wpn_fps_ass_akm_m_magpul/wpn_fps_ass_akm_m_magpul"
-- AKM Gold
if not self.wpn_fps_ass_akm_gold.override then
	self.wpn_fps_ass_akm_gold.override = {}
end
if not self.wpn_fps_ass_akm_gold.override.wpn_fps_upg_ak_m_quick then
	self.wpn_fps_ass_akm_gold.override.wpn_fps_upg_ak_m_quick = {}
end
	self.wpn_fps_ass_akm_gold.override.wpn_fps_upg_ak_m_quick.unit = "units/mods/weapons/wpn_fps_ass_akm_m_magpul/wpn_fps_ass_akm_gold_m_magpul"
-- AKMSU
if not self.wpn_fps_smg_akmsu.override then
	self.wpn_fps_smg_akmsu.override = {}
end
if not self.wpn_fps_smg_akmsu.override.wpn_fps_upg_ak_m_quick then
	self.wpn_fps_smg_akmsu.override.wpn_fps_upg_ak_m_quick = {}
end
	self.wpn_fps_smg_akmsu.override.wpn_fps_upg_ak_m_quick.unit = "units/mods/weapons/wpn_fps_ass_akm_m_magpul/wpn_fps_ass_akm_m_magpul"
if not self.wpn_fps_smg_x_akmsu.override then
	self.wpn_fps_smg_x_akmsu.override = {}
end
if not self.wpn_fps_smg_x_akmsu.override.wpn_fps_upg_ak_m_quick then
	self.wpn_fps_smg_x_akmsu.override.wpn_fps_upg_ak_m_quick = {}
end
	self.wpn_fps_smg_x_akmsu.override.wpn_fps_upg_ak_m_quick.unit = "units/mods/weapons/wpn_fps_ass_akm_m_magpul/wpn_fps_ass_akm_m_magpul"
-- AK-12
if not self.wpn_fps_ass_flint.override then
	self.wpn_fps_ass_flint.override = {}
end
if not self.wpn_fps_ass_flint.override.wpn_fps_upg_ak_m_quick then
	self.wpn_fps_ass_flint.override.wpn_fps_upg_ak_m_quick = {}
end
	self.wpn_fps_ass_flint.override.wpn_fps_upg_ak_m_quick.unit = "units/mods/weapons/wpn_fps_ass_flint_m_magpul/wpn_fps_ass_flint_m_magpul"
end)